n = int(input())
l=[]
for i in range(n):
	l.append(int(input()))

l.sort()

if len(l)==max(l):
	print("good job")
else:
	for i in range(1,max(l)):
		if not i in l:
			print(i)

