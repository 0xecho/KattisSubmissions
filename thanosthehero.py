def isi(l):

	l.sort()
	for i in range(len(l)-1):
		if l[i]>=l[i+1]:
			return 0
		if l[i]<0:
			return 0

	return 1

x = int(input())

l = [int(i)for i in input().split()]
k=0
for i in range(len(l)-1,0,-1):
	if l[i-1]>=l[i]:
		d = l[i-1]-l[i]+1
		l[i-1] -= d
		k+=d
if isi(l):
	print(k)
else:
	print(1)

