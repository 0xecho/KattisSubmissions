inp = input()
key = input()

# key += inp[:max(0,len(inp)-len(key))]
# print(key)
o = ""

for i in range(len(inp)):
	dx = chr( (ord(inp[i]) - ord(key[i]))%26 + 65 )
	key+=dx
	o+=dx
	# print(inp[i], key[i], dx)
	# print((ord(inp[i]) , ord(key[i])),(ord(inp[i]) - ord(key[i])))

print(o)