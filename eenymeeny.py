n = len(input().split())-1

l = []
l1 = []
l2 = []


for _ in range(int(input())):

	l.append(input())


while l:

	x = l[n%len(l)]
	y = l[n%len(l)+1:]
	l1.append(x)
	del l[n%len(l):]
	for i in y[::-1]:
		l.insert(0,i)
	try:

		x = l[n%len(l)]
		y = l[n%len(l)+1:]
		l2.append(x)
		del l[n%len(l):]
		for i in y[::-1]:
			l.insert(0,i)
	except:
		pass
	
print(len(l1))
print(*l1,sep="\n")
print(len(l2))
print(*l2,sep="\n")