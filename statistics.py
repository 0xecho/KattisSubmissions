import sys
c=1
for i in sys.stdin:
	inp=[int(j) for j in i.split()][1:]
	print("Case {}:".format(c),min(inp),max(inp),max(inp)-min(inp))
	c+=1


