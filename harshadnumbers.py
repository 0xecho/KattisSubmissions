import sys
inp=int(input())
while True:
	if inp%sum([int(i)for i in str(inp)])==0:
		print(inp)
		sys.exit()
	inp+=1