def diff(x,y):
	return abs(x[0]-y[0])==abs(x[1]-y[1])
def valid(g):
	sl = []
	for i in range(len(g)):
		if g[i].count("*")!=1:
			return False
		sl.append((i,g[i].index("*")))
	tg = list(map(list, zip(*g)))
	for i in tg:
		if i.count("*")!=1:
			return False
	for i in range(len(tg)-1):
		for j in range(i+1,len(tg)):
			if diff(sl[i],sl[j]):
				# print(sl[i],sl[j])
				return 0
	return 1





g=[]
for i in range(8):
	g.append(list(input()))

print("valid"if valid(g)else "invalid")