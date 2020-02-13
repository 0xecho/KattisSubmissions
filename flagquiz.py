import random
input()

x = int(input())
l=[]

for i in range(x):
	l.append(input().split(", "))
	# l.append(gr())

def diff(a,b):
	cnt=0
	for i,j in enumerate(a):
		if j!=b[i]:
			cnt+=1
	return cnt
d=[0]*x

for i,j in enumerate(l):
	for k,m in enumerate(l):
		if i==k:
			continue
		d[i]=max(d[i], diff(j,m))

for i,j in enumerate(d):
	if j == min(d):
		print(*l[i],sep=", ")

