T = int(input())

for _ in range(T):
	s="Impossible"
	a,b,c=[int(i)for i in input().split()]
	if a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c:
		s="Possible"
	print(s)