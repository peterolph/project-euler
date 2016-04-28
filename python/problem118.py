
import math
import operator
import copy
from bitarray import bitarray

def intsqrt(n):
  return int(math.sqrt(n))

def primes(n):
  sieve = bitarray(n)
  sieve.setall(1)
  for i in xrange(2,intsqrt(n)+1):
    if sieve[i]:
      for m in xrange(2*i,n,i):
        sieve[m] = 0

  return [i[0] for i in enumerate(sieve) if i[1] == 1][2:]


size = 1000000000
pandigits = set('123456789')

buckets = {d:set() for d in pandigits}
for p in primes(size):
  strp = str(p)
  digits = set(strp)
  if len(strp) == len(digits) and digits <= pandigits:
    for d in digits:
      buckets[d].add(strp)
print "Done making primes"
memoise = {}
def find(remaining):
  fr = frozenset(remaining)
  if fr in memoise:
    return memoise[fr]
  used = pandigits - remaining
  out = set.union(*[buckets[d] for d in remaining]) - set.union(*[buckets[d] for d in used])
  memoise[fr] = out
  return out

possibles = {frozenset([p]) for p in buckets['1']}

solutions = set()

while possibles:
  oldpossibles = copy.deepcopy(possibles)
  possibles = set()
  for p in oldpossibles:
    remaining = pandigits - set(''.join(p))
    if not remaining:
      solutions.add(frozenset(p))
    else:
      for f in find(remaining):
        possibles.add(frozenset(set(p) | set([f])))
  print len(possibles),len(solutions)


