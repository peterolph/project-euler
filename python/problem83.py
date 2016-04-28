from heapq import *

class coord(object):
    def __init__(self,x,y):
        self.g = 0
        self.x = x
        self.y = y
    def __lt__(self,other):
        return self.g < other.g
    def __repr__(self):
        return str((self.g,self.x,self.y))
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

class closed_set(object):
    def __init__(self,size):
        self.m = [[False for i in range(size)] for i in range(size)]
    def push(self,i):
        self.m[i.x][i.y] = True
    def __contains__(self,i):
        return self.m[i.x][i.y]

class open_set(object):
    def __init__(self,size):
        self.m = [[False for i in range(size)] for i in range(size)]
        self.q = []
    def push(self,i):
        heappush(self.q,i)
        self.m[i.x][i.y] = True
    def pop(self):
        o = heappop(self.q)
        self.m[o.x][o.y] = False
        return o
    def __contains__(self,i):
        return self.m[i.x][i.y]

m = [[int(x) for x in line.split(',')] for line in open('data/matrix.txt','r').readlines()]
size = 80

g = [[0 for i in range(size)] for i in range(size)]
g[0][0] = m[0][0]

cset = closed_set(size)
oset = open_set(size)

oset.push(coord(0,0))

while oset:
    
    c = oset.pop()

    if c.x == size-1 and c.y == size-1:
        break
    
    cset.push(c)

    ns = []
    if c.x >      0: ns.append(coord(c.x-1,c.y))
    if c.x < size-1: ns.append(coord(c.x+1,c.y))
    if c.y >      0: ns.append(coord(c.x,c.y-1))
    if c.y < size-1: ns.append(coord(c.x,c.y+1))

    for n in ns:
        if n in cset:
            continue
        
        n.g = g[c.x][c.y] + m[n.x][n.y]

        if n not in oset or n.g < g[n.x][n.y]:
            g[n.x][n.y] = n.g
            if n not in oset:
                oset.push(n)

print g[size-1][size-1]
