input()

l = sorted([int(i)for i in input().split()])
x = []
for i in range(len(l)):
	x.append(l[i]/(i+1))

print("impossible" if max(x)>1 else min(x))