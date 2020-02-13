input()
l=[-int(i) for i in input().split() if int(i)<0]
print(sum(l))