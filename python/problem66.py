import math, time

sqs = [x*x for x in range(0,32)]

for D in range(2,100):
    if D in sqs:
        continue
    x = 2
    while True:
        if (x*x-1) % D == 0:
            y2 = (x*x-1)/D
            y = int(math.sqrt(y2))
            if y*y == y2:
                print D,x,y
                break
        x += 1
        if x > 1e8:
            raise Exception

print "THIS IS A RANDOM STRING"
print "THIS IS A DIFFERENT RANDOM STRING"
