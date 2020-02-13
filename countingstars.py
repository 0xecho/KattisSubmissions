import sys
p=[]
def get_adj(l,x,y):

	adjs= []
	if x>0:
		if l[x-1][y] == "-":
			adjs.append([x-1,y])
	if x<len(l)-1:
		if l[x+1][y] == "-":
			adjs.append([x+1,y])
	if y>0:
		if l[x][y-1] == "-":
			adjs.append([x,y-1])
	if y<len(l[0])-1:
		if l[x][y+1] == "-":
			adjs.append([x,y+1])
	
	return adjs


def find(x):
	if p[x]==x:
		return x
	p[x] = find(x)
	return p[x]
def unite(x,y):
	p[find(x)]=find(y);

for i in range(10010):
	p.append(i)

cnum = 1
for i in sys.stdin:

	m,n = [int(i)for i in i.split()]

	vis = [[0 for j in range(n)] for i in range(m)]

	l = []

	for i in range(m):
		l.append(list(input()))

	count = 0

	for i in range(len(l)):
		for j in range(len(l[i])):
			# if l[i][j]=="-":
			# 	add = 1
			# 	adjs = get_adj(l,i,j)
			# 	for val in adjs:
					# rep1,rep2 = (int("".join([str(i),str(j)])), int("".join([str(vals[1]),str(vals[1])])))
			# 		if find(rep1)!=find(rep2):
			# 			add = 0
			# 			unite(rep2,rep1)

			if l[i][j]=="-":
				if vis[i][j]:
					continue
				count+=1
				rep = int("".join([str(i),str(j)]))
				adjs = get_adj(l,i,j)
				vis[i][j] = 1
				
				while adjs:
					# print(adjs)
					x,y = adjs.pop()
					if vis[x][y]:
						continue
					vis[x][y]=1
					for val in get_adj(l,x,y):
						adjs.append([val[0],val[1]])
	print(f"Case {cnum}:",count)
	cnum+=1

					