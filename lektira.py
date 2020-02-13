inp = input()
l="z"*51
for i in range(1,len(inp)-1):
	for j in range(i+1,len(inp)):
		l = min(l,inp[:i][::-1] + inp[i:j][::-1]+ inp[j:][::-1])
		# print(i,j,l)
		# print(inp[:i],inp[i:j],inp[j:])
print(l)