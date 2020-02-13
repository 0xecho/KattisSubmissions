T = int(input())
while T:
	inp = input()
	if inp.startswith("Simon says"):
		print(inp[10:])
	T-=1