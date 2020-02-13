T=int(input())
l=[]
for _ in range(T):
	l.append(input().split())
ll={}
for i in l:
	try:
		if type(int(i[0]))==type(0):
			ll[int(int(i[0])/2)]=i[1]
	except:
		ll[int(i[1])]=i[0]

for i in sorted(ll):
	print(ll[i])

