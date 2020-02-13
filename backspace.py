inp = input()
l=[]
for i in inp:
	if not i=="<":
		l.append(i)
	else:
		l.pop()
print("".join(l))
