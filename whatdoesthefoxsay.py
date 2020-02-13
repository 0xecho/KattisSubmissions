for i in range(int(input())):
	x = input()
	l = []
	inp = input()
	while inp != "what does the fox say?":
		l.append(inp.split()[-1])
		inp = input()


	print(" ".join([i for i in x.split() if not i in l]))
