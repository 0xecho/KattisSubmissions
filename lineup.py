inp = int(input())
l=[]
for _ in range(inp):
	l.append(input())
if(sorted(l)==l):print("INCREASING")
elif(sorted(l,reverse=True)==l):print("DECREASING")
else:print("NEITHER")