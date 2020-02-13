import math
def isp(p):

	if p==2:
		return 1
	if p%2==0:
		return 0
	for i in range(3,int(math.sqrt(p)+1),2):
		if p%i==0:
			return 0
	return 1


def x(p,a):
	return pow(a,p,p) == a


while 1:
	p,a = [int(i)for i in input().split()]

	if not p:
		break


	if not isp(p) and x(p,a):
		print("yes")
	else:
		print("no")
