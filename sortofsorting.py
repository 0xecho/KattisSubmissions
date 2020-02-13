while 1:
	r = int(input())

	if not r:
		break

	l=[]

	for i in range(r):

		l.append(input())

	print(*sorted(l,key=lambda x:x[:2]),sep="\n")
