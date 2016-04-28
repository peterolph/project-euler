
factorials = (1,1,2,6,24,120,720,5040,40320,362880)

def vals():
  v = [0]
  while True:
    
    if v[-1] == 9:
      v.append(0)
    for i in xrange(len(v)-1,-1,-1):
      if v[i] == 9:
        v[i+1] += 1
        v[0:i+1] = [v[i+1]]*(i+1)
        break
    else:
      v[0] += 1
    
    yield v

def listsum(n):      
    out = 0
    mul = 1
    for i in n:
      out += mul * i
      mul *= 10
    return out

def digits(n):
  return [int(x) for x in str(n)]

def digitsum(n):
  return sum(digits(n))

def f(n):
  return sum([factorials[x] for x in n])

def sf(n):
  return digitsum(f(n))

gs = []
v = vals()
t = v.next()
def g(n):
  global t, gs
  gs.extend([0]*(n-len(gs)+1))
  while gs[n] == 0:
    g = sf(t)
    if len(gs) <= g:
      gs.extend([0]*(g-len(gs)+1))
    if gs[g] == 0:
      gs[g] = listsum(t)
    t = v.next()
  return gs[n]

def sg(n):
  return digitsum(g(n))

if __name__ == '__main__':
  total = 0
  for i in range(1,151):
    total += sg(i)
    print i,g(i),sg(i),total
  print gs
