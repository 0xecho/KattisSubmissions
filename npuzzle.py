l=[]
for i in range(4):
	l.append(input())

def f(x,l):
	for i in l:
		if x in i:
			return [l.index(i),i.find(x)]

m=["ABCD","EFGH","IJKL","MNO."]

c=0
for i in m:
	for j in i:

		ff= f(j,l)

		dx=abs(ff[0]-f(j,m)[0])
		dy=abs(ff[1]-f(j,m)[1])
		if not j ==".":
			c+=abs(dx+dy)
print(c)
