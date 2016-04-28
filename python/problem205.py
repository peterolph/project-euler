
import itertools

p = [0] * 37
c = [0] * 37

for i in itertools.product(range(4),repeat=9):
  p[sum(i)+9] += 1

for i in itertools.product(range(6),repeat=6):
  c[sum(i)+6] += 1

pt = sum(p)
ct = sum(c)

tt = pt * ct

probability = 0
for i in range(36):
  probability += float(c[i] * sum(p[i+1:]))/tt

print probability
