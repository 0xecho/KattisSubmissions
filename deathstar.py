x=int(input())
l=[0]*x
for i in range(x):
	inp = input()
	for j in inp.split():
		l[i] |= int(j)

print(*l)



