
import sys

def fibonacci(n):
  v = [1,2]
  for i in range(n-2):
    v.append(v[-1] + v[-2])
  return v

fibs = fibonacci(int(sys.argv[1]))
l = int(sys.argv[1])
def combos(v=0):
  out = []
  for i in range(l-v):
    out.append([fibs[v+i]])
    if i < l-2:
      sub = combos(v+i+2)
      for s in sub:
        out.append([fibs[v+i]]+s)
  return out

arrays = combos()

#print sorted([sum(x) for x in arrays])

print sum((len(x) for x in arrays if sum(x) < 1e7))
