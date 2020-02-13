for _ in range(int(input())):
	n,m,ll = [int(i)for i in input().split()]
	l=[[] for i in range(n+1)]
	k=[]
	kd = [False for i in range(n+1)]
	for _ in range(m):
		x,y = [int(i) for i in input().split()]
		l[x].append(y)
	for _ in range(ll):
		k.append(int(input()))
	c=0
	while k:

		p = k.pop(0)
		if kd[p]:
			continue

		c+=1
		kd[p]=True
		for i in l[p]:
			if not kd[i]:
				k.append(i)
	print(c)


