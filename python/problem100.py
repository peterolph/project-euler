
root2 = 1.4142135623730950488016887242096980785696718753769480

def vals():
    start = 1000000000000
    while True:
        for i in xrange(1000000):
            start += 1
            yield start
        print start

if __name__ == '__main__':
  for n in vals():

    b = int(n/root2)+1
    if (n*(n-1)) == (b*(b-1)) * 2:
        print n,b
