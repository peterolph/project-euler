
import itertools

def getresults(vals):
  vals = [float(x) for x in vals]
  values = itertools.permutations(vals)
  operators = itertools.product('+-*/',repeat=3)
  brackets = ([(0,1)], [(1,2)], [(2,3)], [(0,1),(2,3)],
              [(0,2)], [(1,3)], [(0,2),(0,1)], [(0,2),(1,2)], [(1,3),(1,2)], [(1,3),(2,3)],
              [(0,3)])
  
  results = set()
  for combo in itertools.product(values,operators,brackets):
    v,o,b = combo
    v = [str(i) for i in v]
    for i in b:
      v[i[0]] = '(' + v[i[0]]
      v[i[1]] = v[i[1]] + ')'
    mix = str(v[0]) + o[0] + str(v[1]) + o[1] + str(v[2]) + o[2] + str(v[3])
    try:
      result = eval(mix)
      if result > 0 and result.is_integer():
        results.add(int(eval(mix)))
    except ZeroDivisionError:
      pass
  return results

overall_best = []
overall_max = 0
for combo in itertools.combinations([0,1,2,3,4,5,6,7,8,9],4):
  results = getresults(combo)
  max = 1
  while max in results:
    max += 1
  print combo, max - 1
  if max - 1 > overall_max:
    overall_best = combo
    overall_max = max - 1

print
print overall_best,overall_max

    
  
