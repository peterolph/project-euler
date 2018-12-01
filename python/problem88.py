
import math
import itertools
import sys

def factors(n):
    sqrtn = math.ceil(math.sqrt(n))
    facs = [f for f in range(2,sqrtn) if n%f == 0]
    revs = [n//f for f in facs[::-1]]
    if sqrtn*sqrtn == n:
        facs.append(sqrtn)
    return facs + revs

def factorisations(n, factors):
    for index in range(len(factors)):
        f = factors[index]
        if n == f:
            yield [n]
        elif n%f==0:
            reduced = n//f
            for fact in factorisations(reduced,factors[index:]):
                yield [f] + fact

if __name__ == "__main__":

    K = int(sys.argv[1])

    left = {i for i in range(2,K+1)}
    mins = {}
    
    for n in range(2,K*2+1):
        if len(left) == 0:
            break
        for f in factorisations(n, factors(n)):
            ones = sum(f) - len(f)
            if n - ones in left:
                k = n - ones
                mins[k] = n
                left.remove(k)

    print(sum(set(mins.values())))
