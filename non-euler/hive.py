import random

class Loc(object):
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __getitem__(self,index):
        if index == 0:
            return self.i
        elif index == 1:
            return self.j
        elif index == 2:
            return self.k
        else:
            raise KeyError

    def __add__(self,other):
        return Loc(*[self[i] + other[i] for i in range(3)])

    def __sub__(self,other):
        return Loc(*[self[i] - other[i] for i in range(3)])

    def __str__(self):
        return 'Loc(%s,%s,%s)' % (self.i, self.j, self.k)

    def __repr__(self):
        return str(self)

class Token(object):

    bee = 'bee'
    ant = 'ant'
    grasshopper = 'grasshopper'
    beetle = 'beetle'
    spider = 'spider'
    kinds = (bee, ant, grasshopper, beetle, spider)

    def __init__(self,player,kind,loc=None):
        self.player = player
        self.kind = kind
        self.loc = loc

    def __str__(self):
        return "%s %s %s" % (self.player, self.kind, self.loc and self.loc or '(in hand)')

    def __repr__(self):
        return 'hive_token(%s, %s, %s)' % (self.player, self.kind, self.loc)

    def is_in_hand(self):
        return self.loc is None

    def is_on_board(self):
        return self.loc is not None

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

    def occupied(self):
        return set(self.tokens.keys())

    def neighbours(self,loc):
        x,y = loc
        offsets = ((1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1))
        return set((x+ox,y+oy) for ox,oy in offsets)

    def neighbour_tokens(self,loc):
        return [self.tokens[neighbour] for neighbour in self.neighbours(loc) if neighbour in self.tokens]

    def neighbours_occupied(self,loc):
        return self.neighbours(loc) & self.occupied()

    def __str__(self):
        return 'Board state: ' + str(self.tokens)

    def get_tokens(self, player=None):
        if player:
            return set(token for token in self.tokens.values() if token.player == player)
        else:
            return set(self.tokens.values())

    def count(self, player=None):
        return len(self.get_tokens(player))

class Game(object):

    white = 'white'
    black = 'black'
    players = (white, black)

    draw = 'draw'

    starting_hand = tuple([Token.bee] + [Token.grasshopper]*3 + [Token.ant]*3 + [Token.beetle]*2 + [Token.spider]*2)

    def __init__(self):
        self.board = Board()
        self.tokens = {player:[Token(player,kind) for kind in self.starting_hand] for player in self.players}
        self.bee = {player:self.tokens[player][0] for player in self.players}
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
            bee = self.bee[player]
            if bee.is_on_board() and len(self.board.neighbour_tokens(bee)) == 6:
                winners.append(self.opponent[player])
        if len(winners) == 0:
            return None
        elif len(winners) == 1:
            return winners[0]
        else:
            return Game.draw

    def placed_tokens(self, player):
        return [token for token in self.tokens[player] if token.is_on_board()]

    def merge(self, iterable_of_sets):
        return reduce(lambda a,b: a|b, iterable_of_sets, set())

    def player_neighbours(self, player):
        return self.merge(self.board.neighbours(token.loc) for token in self.board.get_tokens(player))

    def opponent(self,player):
        if player == Game.white:
            return Game.black
        else:
            return Game.white

    def valid_destinations(self,token):
        if token.is_in_hand():
            if self.board.count() == 0:
                # First token: only one valid location
                return set([(0,0)])

            elif self.board.count() == 1:
                # Second token: is allowed to touch opponent token
                return self.board.neighbours((0,0))

            elif self.board.count(token.player) == 3 and self.bee[token.player].is_in_hand() and token.kind != Token.bee:
                # If three tokens have been placed but not the bee, must place the bee
                return set()

            else:
                # Normal situation: token can be placed on any free space that touches own token but not opponent's
                return self.player_neighbours(token.player) - self.player_neighbours(self.opponent(token.player)) - self.board.occupied()

        else:
            if self.bee[token.player].is_in_hand():
                # Cannot move tokens if the bee has not been played
                return set()

            elif self.board.trapped(token):
                # Cannot move a token if it would split the hive
                return set()

            elif token.kind == Token.bee:
                return set()
            elif token.kind == Token.ant:
                return set()
            elif token.kind == Token.grasshopper:
                return set()
            elif token.kind == Token.beetle:
                return set()
            elif token.kind == Token.spider:
                return set()

    def valid_moves(self, player):
        return [(token,self.valid_destinations(token)) for token in self.tokens[player]]

    def random_move(self, player):
        token, moves = random.choice(filter(lambda (token,moves): moves, self.valid_moves(player)))
        move = random.choice(tuple(moves))
        return (token, move)

    def pretty_print_moves(self,moves):
        return '\n'.join(str(token) + ' -> ' + ", ".join(str(dest) for dest in destinations) for token, destinations in moves)

if __name__ == "__main__":
    g = Game()

    g.move(g.bee[Game.white],(0,0))
    g.move(g.bee[Game.black],(0,1))
    g.move(*g.random_move(Game.white))

    print g.pretty_print_moves(g.valid_moves(Game.white))
