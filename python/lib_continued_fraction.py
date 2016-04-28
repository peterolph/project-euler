
import math

def getsqrt(n):
    k = [int(math.sqrt(n))]

    if k[0]*k[0] == n:
        return k
    
    a = 1
    b = k[0]
    while k[-1] != 2*k[0]:
        
        a = (n - b*b) / a
        k.append( (k[0] + b) / a )
        b = k[-1] * a - b
    
    return k
