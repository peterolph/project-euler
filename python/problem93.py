
import itertools

a = [1.0,2.0,3.0,4.0]
operators = ["+","-","*","/"]

out = []
for vals in itertools.permutations(a):
  for ops in itertools.product(operators,repeat=3):
    string = str(vals[0])+ops[0]+str(vals[1])+ops[1]+str(vals[2])+ops[2]+str(vals[3])
    #print string
    val = eval(string)
    if int(val) not in out:
      out.append(int(val))

print len(out)
print sorted(out)
