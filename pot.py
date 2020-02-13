T = int(input())
s=0
while T:
	inp = input()
	s+=int(inp[:-1])**int(inp[-1])
	T-=1
print(s)