import random

class Token(object):

    def __init__(self,player,kind,loc=None):
        self.player = player
        self.kind = kind
        self.loc = loc

    def is_in_hand(self):
        return self.loc is None

    def is_on_board(self):
        return self.loc is not None

    def __str__(self):
        return "%s %s %s" % (self.player, self.kind, self.loc and self.loc or '(in hand)')

    def __repr__(self):
        return str(self)

class Board(object):

    def __init__(self):
        self.tokens = {}

    def add(self,token):
        self.tokens[token.loc] = token

    def remove(self,token):
        del self.tokens[token.loc]

    def trapped(self,token):
        openset = [self.neighbour_tokens(token.loc)[0]]
        closedset = [token]
        while openset:
            current = openset.pop()
            closedset.append(current)
            openset.extend([neighbour for neighbour in self.neighbour_tokens(current.loc) if neighbour not in closedset])
        return len(closedset) < len(self.tokens)

    def occupied_hexes(self):
        return set(self.tokens.keys())

    def neighbour_hexes(self,loc):
        x,y = loc
        offsets = ((1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1))
        return set((x+ox,y+oy) for ox,oy in offsets)

    def occupied_neighbour_hexes(self,loc):
        return self.neighbour_hexes(loc) & self.occupied_hexes()

    def neighbour_tokens(self,loc):
        return [self.tokens[neighbour] for neighbour in self.occupied_neighbour_hexes(loc)]

    def __str__(self):
        return 'Board state: ' + str(self.tokens)

    def get_tokens(self, player=None):
        if player:
            return set(token for token in self.tokens.values() if token.player == player)
        else:
            return set(self.tokens.values())

    def count_tokens(self, player=None):
        return len(self.get_tokens(player))

class Player(object):

    def __init__(self, colour, starting_hand):
        self.colour = colour
        self.tokens = [Token(self,kind) for kind in starting_hand]
        self.bee = self.tokens[0]

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
        self.turn = 0

    def move(self,token,destination):
        if token.is_on_board():
            self.board.remove(token)
        token.loc = destination
        self.board.add(token)
        print self.board

    def winner(self):
        winners = []
        for player in self.players:
            if player.bee.is_on_board() and len(self.board.neighbour_tokens(player.bee)) == 6:
                winners.append(self.opponent[player])
        return winners

    def merge(self, iterable_of_sets):
        return reduce(lambda a,b: a|b, iterable_of_sets, set())

    def player_neighbours(self, player):
        return self.merge(self.board.neighbour_hexes(token.loc) for token in self.board.get_tokens(player))

    def opponent(self,player):
        if player.colour == Game.white:
            return self.players[Game.black]
        else:
            return self.players[Game.white]

    def valid_destinations(self,token):
        player = token.player
        opponent = self.opponent(player)

        if token.is_in_hand():
            if self.board.count_tokens() == 0:
                # First token: only one valid location
                return set([(0,0)])

            elif self.board.count_tokens() == 1:
                # Second token: is allowed to touch opponent token
                return self.board.neighbours((0,0))

            elif self.board.count_tokens(player) == 3 and player.bee.is_in_hand() and token.kind != Game.bee:
                # If three tokens have been placed but not the bee, must place the bee
                return set()

            else:
                # Normal situation: token can be placed on any free space that touches own token but not opponent's
                return self.player_neighbours(player) - self.player_neighbours(opponent) - self.board.occupied_hexes()

        else:
            if player.bee.is_in_hand():
                # Cannot move tokens if the bee has not been played
                return set()

            elif self.board.trapped(token):
                # Cannot move a token if it would split the hive
                return set()

            elif token.kind == Game.bee:
                return set()
            elif token.kind == Game.ant:
                return set()
            elif token.kind == Game.hopper:
                return set()
            elif token.kind == Game.beetle:
                return set()
            elif token.kind == Game.spider:
                return set()

    def valid_moves(self, player):
        return [(token,self.valid_destinations(token)) for token in player.tokens]

    def random_move(self, player):
        token, moves = random.choice(filter(lambda (token,moves): moves, self.valid_moves(player)))
        move = random.choice(tuple(moves))
        return (token, move)

    def pretty_print_moves(self,moves):
        return '\n'.join(str(token) + ' -> ' + ", ".join(str(dest) for dest in destinations) for token, destinations in moves)

if __name__ == "__main__":
    g = Game()

        g.move(g.players[Game.white].bee, (0,0))
        g.move(g.players[Game.black].bee, (0,1))
        g.move(*g.random_move(g.players[Game.white]))

        print g.pretty_print_moves(g.valid_moves(g.players[Game.white]))
