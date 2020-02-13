l=[]
for i in range(3):
	l += [int(i)for i in input().split()]
l1=[i for i in l[::2]]
l2=[i for i in l[1::2]]
for i in l1:
	if l1.count(i)==1:
		print(i,end=" ")
for i in l2:
	if l2.count(i)==1:
		print(i)

