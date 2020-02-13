inp = [int(i) for i in input().split()]
if inp[1]>=45:
	print(inp[0],inp[1]-45)
else:
	if inp[0]==0:
		print(23,60-45+inp[1])
	else:
		print(inp[0]-1,60-45+inp[1])
