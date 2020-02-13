x = input()
o=x
v=0
for i in range(1,len(x)//2 + 1):
	# print(i)
	if len(x)%i==0:
		v=1
		ws = []
		dx = len(x)//i
		for j in range(dx):
			if j==0:
				o = x[j*i:i*j+i]
			ws.append(sorted(x[j*i:i*j+i]))

		p=ws[0]
		
		for i in ws[1:]:
			if not i == p:
				v=0
				break
			# print(i,p,i==p)
			p=i
		# print(ws,p,v)
	# print(ws,o,v)
	if v:
		break
if len(x)==1:
	print(x)		
elif v:
	print("".join(o))
else:
	print("-1")
