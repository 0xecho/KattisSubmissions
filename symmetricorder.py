T = int(input())
n=1
while T:
	l,r=[],[]
	c=2
	for i in range(T):
		s=input()
		if c%2:
			r=[s]+r
		else:
			l+=[s]
		c+=1
	print("SET",n)
	n+=1
	for i in l+r:
		print(i) 
	T=int(input())