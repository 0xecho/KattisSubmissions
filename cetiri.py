import sys
a,b,c = [int(i)for i in input().split()]

m = min(abs(a-b),abs(b-c))
l=sorted([a,b,c])
for i in range(len(l)-1):
	if l[i]+m==l[i+1]:
		continue
	print(l[i]+m)
	sys.exit()
print(l[i+1]+m)