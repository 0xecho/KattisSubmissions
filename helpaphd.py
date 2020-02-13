for i in range(int(input())):
	inp=input()
	if "+"in inp:
		a,b=[int(i) for i in inp.split("+")]
		print(a+b)
	else:
		print("skipped")
