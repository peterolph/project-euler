

def poly(coefficients,x):
  y = 0
  p = 1
  for c in coefficients:
    y += c * p
    p *= x
  return y

def target(x):
  return poly([1,-1,1,-1,1,-1,1,-1,1,-1,1],x)

data = [target(x) for x in xrange(1,11)]


