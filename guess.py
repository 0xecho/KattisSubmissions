l=1
h=1001
while True:
    m=(l+h)/2
    print(int(m))
    x = input()
    if x=="lower":
        h=m
    elif x=="higher":
        l=m
    else:
        break