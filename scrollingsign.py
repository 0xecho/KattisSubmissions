def inn(a,b):
	if a==b:
		return ""
	for i in range(len(b)):
		i = -i
		# print("here",i,b[:i],a)
		if not len(b[:i]):
			continue

		if a.endswith(b[:i]):
			return b[i:]
	return b

for _  in range(int(input())):

	x,y= [int(i)for i in input().split()]

	s=""

	for _ in range(y):

		x = input()
		i=0
		if _ == 0:
			s+=x
			continue
		# print(i,x[i],s[-i-1])
		# print(inn)
		s+=inn(s,x)
		# while x[i]==s[-i-1]:
		# 	print(i)
		# 	i+=1
		# s+=x[i:]
	print(len(s))
