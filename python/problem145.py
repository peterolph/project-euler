
count = 0
for i in xrange(1000000000):
  if i%10 != 0:
    s = str(i + int(str(i)[::-1]))
    if '0' not in s and '2' not in s and '4' not in s and '6' not in s and '8' not in s:
      count += 1

print count
