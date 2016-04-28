
ways = [0, 1, 2, 3, 5, 7]

for i in range(6,10):
  t = 1
  for j in range(i,(i-1)/2,-1):
    t += ways[i-j]
  ways.append(t)

print ways

"""
o

oo
o o

ooo
oo o
o o o

oooo
ooo o
oo oo
oo o o
o o o o

ooooo
oooo o
ooo oo
ooo o o
oo oo o
oo o o o
o o o o o
"""
