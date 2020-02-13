_,__ = input().split()

l = [int(i)for i in input().split()]
nl=[]

def k(x):
	return l.count(x)
l=sorted(l,key=k,reverse=True)
# print(l)
for i in l:
	if i not in nl:
		for j in range(l.count(i)):
			nl.append(i)
print(*nl)