import sys
for inp in sys.stdin:
    a = [int(i) for i in inp.split()]
    for i in a:
        if i==sum(a[:a.index(i)]+a[a.index(i)+1:]):
            print(i)
            break
            
