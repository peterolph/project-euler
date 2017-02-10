import random
import hexes

def merge_sets(iterable_of_sets):
    return reduce(lambda a,b: a|b, iterable_of_sets, set())

class Token(object):

    def __init__(self,player,kind,hex=None):
        self.player = player
        self.kind = kind
        self.hex = hex

    def is_in_hand(self):
        return self.hex is None

    def is_on_board(self):
        return self.hex is not None

    def __str__(self):
        return "%s %s %s" % (self.player, self.kind, self.hex and self.hex or '(in hand)')

    def short_string(self):
        return "%s%s" % (self.player.colour[0], self.kind == 'bee' and 'B' or self.kind[0])

    def __repr__(self):
        return str(self)

class InvalidMove(Exception):
    pass

class Board(object):

    def __init__(self):
        self.tokens = {}

    def add(self,token, destination):
        self.tokens[destination] = token

    def remove(self,token):
        del self.tokens[token.hex]

    def trapped(self,token):
        # Would removing this token split the hive?
        neighbours = self.occupied_neighbour_hexes(token.hex)
        if len(neighbours) == 0:
            return False
        else:
            openset = [neighbours.pop()]
            closedset = [token.hex]
            while openset:
                current = openset.pop()
                closedset.append(current)
                openset.extend([neighbour for neighbour in self.occupied_neighbour_hexes(current) if neighbour not in closedset])
            return len(closedset) < len(self.tokens)

    def occupied_hexes(self):
        # any hex occupied on the board
        return set(self.tokens.keys())

    def occupied_neighbour_hexes(self,hex):
        return hexes.neighbours(hex) & self.occupied_hexes()

    def crawl_move(self,hex,pivot,dir):
        offset = hexes.sub(hex,pivot)
        rotated = hexes.rotate(offset,dir)
        target = hexes.add(pivot,rotated)
        blocker = hexes.add(hex,rotated)
        if (pivot in self.tokens and
            target not in self.tokens and
            blocker not in self.tokens):
            return target
        else:
            raise InvalidMove

    def all_crawl_moves(self,hex,dir,disallowed=None):
        moveset = set()
        for neighbour in self.occupied_neighbour_hexes(hex):
            if neighbour != disallowed:
                try:
                    moveset.add(self.crawl_move(hex,neighbour,dir))
                except InvalidMove:
                    pass
        return moveset

    def bee_moves(self,hex):
        # hexes reachable in one crawl move
        return merge_sets([self.all_crawl_moves(hex,'left'), self.all_crawl_moves(hex,'right')])

    def ant_moves(self,hex):
        moveset = self.all_crawl_moves(hex,'right')
        openset = self.all_crawl_moves(hex,'left')
        while openset:
            current = openset.pop()
            moveset.add(current)
            for move in self.all_crawl_moves(current,'left',hex):
                if move not in moveset:
                    openset.add(move)
        return moveset

    def hopper_moves(self,hex):
        moveset = set()
        for neighbour in self.occupied_neighbour_hexes(hex):
            hop_direction = hexes.opposite(hexes.sub(hex,neighbour))
            target = hexes.add(neighbour, hop_direction)
            while target in self.tokens:
                target = hexes.add(target, hop_direction)
            moveset.add(target)
        return moveset

    def spider_moves(self,hex):
        left_moves = right_moves = set([hex])
        for _ in xrange(3):
            left_moves = merge_sets(self.all_crawl_moves(move,'left') for move in left_moves)
            right_moves = merge_sets(self.all_crawl_moves(move,'right') for move in right_moves)
        return left_moves | right_moves

    def beetle_moves(self,hex):
        moveset = set()
        return merge_sets([moveset,self.bee_moves(hex)])

    def neighbour_tokens(self,hex):
        return [self.tokens[neighbour] for neighbour in self.occupied_neighbour_hexes(hex)]

    def count_tokens(self):
        return len(self.tokens)

    def __str__(self):
        minx = min([token.hex[0] for token in self.tokens.values()])
        maxx = max([token.hex[0] for token in self.tokens.values()])
        miny = min([token.hex[0]+2*token.hex[1] for token in self.tokens.values()])
        maxy = max([token.hex[0]+2*token.hex[1] for token in self.tokens.values()])
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                if (y-x)%2==0:
                    try:
                        print self.tokens[(x,(y-x)/2)].short_string(),
                    except KeyError:
                        print '--',
                else:
                    print '  ',
                print ' ',
            print

class Player(object):

    def __init__(self, colour, starting_hand):
        self.colour = colour
        self.tokens = [Token(self,kind) for kind in starting_hand]
        self.bee = self.tokens[0]
        self.human = True

    def tokens_on_board(self):
        return [token for token in self.tokens if token.is_on_board()]

    def __repr__(self):
        return self.colour

class Game(object):

    white = 'white'
    black = 'black'
    colours = (white, black)

    bee = 'bee'
    hopper = 'hopper'
    ant = 'ant'
    beetle = 'beetle'
    spider = 'spider'
    kinds = (bee, hopper, ant, beetle, spider)
    starting_hand = (bee, hopper, hopper, hopper, ant, ant, ant, beetle, beetle, spider, spider)

    def __init__(self):
        self.board = Board()
        self.players = {colour: Player(colour, Game.starting_hand) for colour in Game.colours}
        self.active = self.players[Game.white]
        self.turn = 0

    def move(self,token,destination):
        #print str(token) + ' --> ' + str(destination)
        if token.is_on_board():
            self.board.remove(token)
        self.board.add(token, destination)
        token.hex = destination
        self.active = self.opponent(self.active)
        self.turn += 1
        if len(self.board.occupied_neighbour_hexes(token.hex)) == 0 and len(self.board.tokens) > 1:
            print self.board
            print token, destination
            raise InvalidMove

    def winner(self):
        winners = []
        for player in self.players:
            if player.bee.is_on_board() and len(self.board.neighbour_tokens(player.bee.hex)) == 6:
                winners.append(self.opponent[player])
        return winners


    def player_neighbours(self, player):
        return merge_sets(hexes.neighbours(token.hex) for token in player.tokens_on_board())

    def opponent(self,player):
        if player == self.players[Game.white]:
            return self.players[Game.black]
        else:
            return self.players[Game.white]

    def valid_destinations(self,token):
        player = token.player
        opponent = self.opponent(player)

        if token.is_in_hand():

            # First token: only one valid location
            if self.board.count_tokens() == 0:
                return set([hexes.centre])

            # Second token: is allowed to touch opponent token
            elif self.board.count_tokens() == 1:
                return hexes.neighbours(hexes.centre)

            # If three tokens have been placed but not the bee, must place the bee
            elif len(player.tokens_on_board()) == 3 and player.bee.is_in_hand() and token.kind != Game.bee:
                return set()

            # Normal situation: token can be placed on any free space that touches own token but not opponent's
            else:
                return self.player_neighbours(player) - self.player_neighbours(opponent) - self.board.occupied_hexes()

        else:

            # Cannot move tokens if the bee has not been played
            if player.bee.is_in_hand():
                return set()

            # Cannot move a token if it would split the hive
            elif self.board.trapped(token):
                return set()

            # Normal situation: token can be moved according to its rules
            elif token.kind == Game.bee:
                return self.board.bee_moves(token.hex)
            elif token.kind == Game.ant:
                return self.board.ant_moves(token.hex)
            elif token.kind == Game.hopper:
                return self.board.hopper_moves(token.hex)
            elif token.kind == Game.beetle:
                return self.board.beetle_moves(token.hex)
            elif token.kind == Game.spider:
                return self.board.spider_moves(token.hex)

    def valid_moves(self, player=None):
        if player is None:
            player = self.active
        return [(token, destination) for token in player.tokens for destination in self.valid_destinations(token)]

    def random_move(self, player=None):
        move = random.choice(self.valid_moves(player))
        self.move(*move)

    def pretty_print_moves(self,player=None):
        coalesce = {}
        moves = self.valid_moves(player)
        for token, destination in moves:
            if token not in coalesce:
                coalesce[token] = []
            coalesce[token].append(destination)
        hand_tokens = []
        hand_placements = []
        lines = []
        for token, destinations in coalesce.items():
            if token.is_in_hand():
                hand_tokens.append(token.kind)
                hand_placements = destinations
            else:
                lines.append(str(token) + ' -> ' + str(destinations))
        return ("-----\n" +
                "it is %s's move\n" % moves[0][0].player.colour +
                "hand: %s\n" % str(hand_tokens) + 
                "place: %s\n" % str(hand_placements) + 
                "\n".join(lines))

if __name__ == "__main__":
    count = 0
    fail = 0
    for _ in xrange(1000):
        count += 1
        try:
            game = Game()
            #print '#############################'
            for i in range(23):
                game.random_move()
        except IndexError:
            print count
            print game.board
            print game.board.count_tokens()
            raise
