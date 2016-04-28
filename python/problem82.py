
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

#m = ((131, 673, 234, 103,  18),
#     (201,  96, 342, 965, 150),
#     (630, 803, 746, 422, 111),
#     (537, 699, 497, 121, 956),
#     (805, 732, 524,  37, 331))
#size = 5

m = [[int(x) for x in line.split(',')] for line in open('data/matrix.txt','r').readlines()]
size = 80

mins = []
for i in range(size):
    g = [[0 for z in range(size)] for z in range(size)]
    g[i][0] = m[i][0]

    cset = []
    oset = []

    heappush(oset,coord(i,0))

    while oset:
        
        c = heappop(oset)

        if c.y == size-1:
            mins.append(c.g)
            break
        
        cset.append(c)

        ns = []
        if c.x >      0: ns.append(coord(c.x-1,c.y))
        if c.x < size-1: ns.append(coord(c.x+1,c.y))
        #if c.y >      0: ns.append(coord(c.x,c.y-1))
        if c.y < size-1: ns.append(coord(c.x,c.y+1))

        for n in ns:
            if n in cset:
                continue
            
            n.g = g[c.x][c.y] + m[n.x][n.y]

            if n not in oset or n.g < g[n.x][n.y]:
                g[n.x][n.y] = n.g
                if n not in oset:
                    heappush(oset,n)
    print mins[i]

#print mins
print min(mins)
    





            
