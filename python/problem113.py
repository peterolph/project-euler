
ascends = {}
def countascend(digits,possibilities):
  l = len(possibilities)
  if digits == 1:
    return l
  if (digits,l) in ascends:
    return ascends[(digits,l)]
  retval = 0
  for p in possibilities:
    retval += countascend(digits-1,[pos for pos in possibilities if pos >= p])
  ascends[(digits,l)] = retval
  return retval

descends = {}
def countdescend(digits,possibilities):
  l = len(possibilities)
  if digits == 1:
    return l
  if (digits,l) in descends:
    return descends[(digits,l)]
  retval = 0
  for p in possibilities:
    retval += countdescend(digits-1,[pos for pos in possibilities if pos <= p])
  descends[(digits,l)] = retval
  return retval

def count(digits):
  return sum([countascend(d,[1,2,3,4,5,6,7,8,9]) + countdescend(d,[0,1,2,3,4,5,6,7,8,9]) - 10 for d in range(1,digits+1)])


print count(100)
