
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

ways = [[],[],[[2]],[[3]],[[2,2]],[[3,2],[5]]]

for i in range(6,100):
  t = []
  if i in primes:
    t.append([i])
  for p in primes:
    if p > i:
      break
    for sub in ways[i-p]:
      t.append([p]+sub)
  t = [list(x) for x in set(tuple(sorted(x)) for x in t)]
  ways.append(t)
  if len(ways[i]) > 5000:
    print i,len(ways[i]),len(ways[i-1])
    break

for i in range(50,len(ways)):
  print i,len(ways[i])
