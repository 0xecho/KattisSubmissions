import math
while 1:
	inp = input()

	if inp ==".":
		break
	mx = -1
	for i in range(1,int(math.sqrt(len(inp))+1)):
		if len(inp)%i==0:
			if inp[:len(inp)//i]*i == inp:
				mx = max(mx,i)
			if inp[:i]*(len(inp)//i) == inp:
				mx = max(mx,len(inp)//i)
			# print(mx,i)

	print(mx)