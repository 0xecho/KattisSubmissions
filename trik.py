inp = input()
x=0
for i in range(len(inp)):
	if inp[i]=="A":
		if x==0:
			x+=1
		elif x==1:
			x-=1
	elif inp[i]=="B":
		if x==1:
			x+=1
		elif x==2:
			x-=1
	else:
		if x==0:
			x+=2
		elif x==2:
			x-=2
print(x+1)