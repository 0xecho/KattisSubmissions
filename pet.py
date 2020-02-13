l=[]
for i in range(5):
	l.append(sum(int(i) for i in input().split()))
m=max(l)
print(l.index(m)+1,m)