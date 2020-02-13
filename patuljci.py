import sys
l=[]

def without(l,x):
	m=l	
	for i in x:
		m = m[:m.index(i)]+m[m.index(i)+1:]
	return m

for i in range(9):
	l.append(int(input()))
# print(l)
for i in l:
	for j in without(l,[i]):
		if sum(without(l,[i,j]))==100:
			print(*without(l,[i,j]),sep="\n")
			sys.exit()