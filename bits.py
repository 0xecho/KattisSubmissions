for _ in range(int(input())):
	x=input()
	mx = 0
	for i in range(1,len(x)+1):

		mx = max(mx,(bin(int(x[:i]))[2:].count("1")))

	print(mx)
