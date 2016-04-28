
import sys

def get_cubes(n):
  sqs_set = {x*x:x for x in xrange(n*3+1)}
  pairs = [(a,b) for a in xrange(1,n+1) for b in xrange(1,n*2+1) if a*a + b*b in sqs_set and a + b <= n*3 and a <= n and 2*a >= b]
  count = 0
  for a,b in set(pairs):
    if b <= a:
      count += b/2
    else:
      count += a - (b+1)/2 + 1
  return count

def binsearch(func):
  """Find the lowest value that makes func return True"""
  lo, hi = 0, 1
  while not func(hi):
    lo, hi = hi, hi * 2
  while hi-lo > 1:
    mid = (lo+hi)/2
    if func(mid):
      hi = mid
    else:
      lo = mid
  return hi
  

print binsearch(lambda n: get_cubes(n) > int(sys.argv[1]))

