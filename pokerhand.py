T = input().split()
m=0
p=''
c=0
for i in sorted(T):
	if i[0]==p:
		c+=1
	else:
		p=i[0]
		m=max(m,c)
		c=1
m=max(m,c)

print(m)
