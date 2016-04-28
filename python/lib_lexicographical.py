
def vals():
  v = [0,0,0]
  while True:
    
    if v[-1] == 9:
      v.append(0)
    for i in range(len(v)-1)[::-1]:
      if v[i] == 9:
        v[i+1] += 1
        for j in range(i+1):
          v[j] = v[i+1]
        break
    else:
      v[0] += 1
      
    out = 0
    mul = 1
    for i in v:
      out += mul * i
      mul *= 10
    yield out

v = vals()
x = 1000000
t = 0
for i in range(10):
  print i*x, t
  for j in range(x):
    t = v.next()

"""
1 2 3 4 5 6 7 8 9
11 12 13 14 15 16 17 18 19
22 23 24 25 26 27 28 29 
33 34 35 36 37 38 39 
44 45 46 47 48 49 
55 56 57 58 59 
66 67 68 69 
77 78 79 
88 89 
99
111"""
