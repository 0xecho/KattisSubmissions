for _ in range(int(input())):
	a,b,c = map(int,input().split())
	k=0
	while c >= pow(b,k)*a:
		k+=1

	print(k) 