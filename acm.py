l=[]
t=0
c=0
while True:
	inp = input()
	if inp == "-1":
		break
	l.append(inp.split(' '))

for val in l:
	if val[2] == "right":
		t+=int(val[0])
		t+=sum([20 for i in l if i[0]<=val[0] and i[1]==val[1] and i[2]=="wrong"])
		c+=1


print(c,t)