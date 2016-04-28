
import math
import operator

def intsqrt(n):
  return int(math.sqrt(n))

def primes(n):
  sieve = [True] * n

  for i in xrange(2,intsqrt(n)+1):
    if sieve[i]:
      for m in xrange(2*i,n,i):
        sieve[m] = False

  return [i[0] for i in enumerate(sieve) if i[1] == True][2:]

def product(l):
  return reduce(operator.mul, l, 1)

if True:
  
  n = 120000
  
  p = primes(n)
  d = [[] for i in xrange(n+1)]
  for prime in p:
    for m in xrange(prime,n,prime):
      d[m].append(prime)
  
  d = [set(i) for i in d]
  
  output = []
  for a in xrange(1,n):
    for b in xrange(a+1,n-a):
      c = a + b
      if c > n:
        break
      if not d[a] & d[b] and not d[a] & d[c] and not d[b] & d[c] and product(d[a] | d[b] | d[c]) < c:
        output.append((a,b,c))
        print a,b,c
  print sum([i[2] for i in output])
  
