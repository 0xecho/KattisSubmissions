import math
inp =[int(i) for i in input().split()]
inp = inp[0]/math.sin(inp[1]*3.14159265353/180)
if inp>int(inp):
	inp = int(inp)+1
print(int(inp))