while 1:
	inp = input()
	if inp=="END":
		break

	# inp = int(inp)
	c=0
	while inp!="1":
		inp = str(len(inp))
		
		c+=1

	print(c+1)
	# print(len(str(inp)))