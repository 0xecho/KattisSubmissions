input()
inp=input().split()
b=True
p=0
for i in inp:
	try:
		i=int(i)
		if not p+1==i and b:
			b=False
			print("something is fishy")
		else:
			p+=1
	except:
		p+=1
if b:
	print("makes sense")