
import itertools

sprimes = [2,3,5]
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

#        123456789
limit = 1000000000

count = 0
for i in xrange(1,limit):
  n = i
  for p in primes:
    while n % p == 0:
      n /= p
  if n == 1:
    count += 1

print count
