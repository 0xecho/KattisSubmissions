l = [int(i)for i in input().split()]
x = [1,2,3,4,5]

while l!=x:
	for i in range(len(l)-1):
		j=i+1
		if l[i]>l[j]:
			l[i],l[j] = l[j],l[i] 
			print(*l)
