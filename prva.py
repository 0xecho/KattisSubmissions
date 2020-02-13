a,b = [int(i) for i in input().split()]
l=[]
w=[]
for i in range(a):
	l.append(input())

for i in l:
	for j in i.split("#"):
		if len(j)>=2:
			w.append(j)

for i in map(list,zip(*l)):
	for j in "".join(i).split("#"):
		if len(j)>=2:
			w.append(j)

print(sorted(w)[0])