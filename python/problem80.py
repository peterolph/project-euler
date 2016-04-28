
def sqrt_digits(n, d):
  limit = 10 ** (d+1)
  a = 5 * n
  b = 5
  
  while b < limit:
    if a >= b:
      a -= b
      b += 10
    else:
      a *= 100
      b = (b/10) * 100 + 5
  
  return b/100

def digit_sum(n):
  o = 0
  while n:
    o += n % 10
    n  = n / 10
  return o

if __name__ == '__main__':
  count = 0
  for i in range(1,101):
    if i not in (1,4,9,16,25,36,49,64,81,100):
      count += digit_sum(sqrt_digits(i,100))
  print count
    
      
    
