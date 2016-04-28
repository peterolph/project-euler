import random

def get_n_max(a,n):
    out = [-1] * n
    for i in range(len(a)):
        for j in range(n):
            if out[j] == -1 or a[i] > a[out[j]]:
                for k in range(n-1,j,-1):
                    out[k] = out[k-1]
                out[j] = i
                break
    return out

c = 0

t = 0
n = [0] * 40

cc = 0;
ch = 0;
for i in range(10000000):
    for z in range(3):
        r = (random.randrange(4),random.randrange(4))
        c = c + r[0] + r[1] + 2
        if r[0] != r[1]:
            break
    else:
        r = -1

    c = c % 40
    
    if r == -1: # triple double
        c = 10
    elif c == 30: # go to jail
        c = 10
    elif c in (2,17,33): # community chest
        cc = random.randrange(16)
        if cc == 0: # GO
            c = 0
        elif cc == 8: # jail
            c = 10
    elif c in (7,22,36): # chance
        ch = random.randrange(16)
        if ch == 0: # GO
            c = 0
        elif ch == 1: # jail
            c = 10
        elif ch == 2: # C1
            c = 11
        elif ch == 3: # E3
            c = 24
        elif ch == 4: # H2
            c = 39
        elif ch == 5: # R1
            c = 5
        elif ch == 6: # next R
            c = {7:15, 22:25, 36:5}[c]
        elif ch == 7: # next R
            c = {7:15, 22:25, 36:5}[c]
        elif ch == 8: # next U
            c = {7:12, 22:28, 36:12}[c]
        elif ch == 9: # back 3
            c = (c-3+40)%40

    t    += 1
    n[c] += 1

for i in range(len(n)):
    print i,n[i]
print
for i in get_n_max(n,3):
    print i, float(n[i]*100)/t
