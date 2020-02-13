inp = input()
l=len(inp)
u="per"*100
for i in range(len(inp)):
	if inp[i].lower()==u[i].lower():
		l-=1
print(l)