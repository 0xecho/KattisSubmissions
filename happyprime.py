import math
def sqr(x):
	return pow(int(x),2)
def is_happy(x):
	vals = []
	s=x
	for i in range(100):
		s = sum(map(sqr,str(s)))
		if s==1:
			return 1
		if s in vals:
			return 0
		vals.append(s)
	
def is_prime(x):
	if x==1:
		return 0
	if x==2:
		return 1
	if x%2==0:
		return 0
	# print(x)
	for i in range(3,int(math.sqrt(x))+1):
		if x%i==0:
			return 0
	return 1
for _ in range(int(input())):
	a,b = [int(i)for i in input().split()]

	# print(is_prime(b))
	print(a,b,"YES" if is_prime(b)and is_happy(b) else "NO")