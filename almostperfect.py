from math import sqrt
def d(n):
	l=set([1])
	for i in range(2,int(sqrt(n)+1)):
		if n%i==0:
			l.add(i)
			l.add(n/i)
			continue
	return l

while True:
	try:
		inp = int(input())
		r=int(sum(d(inp)))
		if(r==inp):
			o="perfect"
		elif(abs(r-inp)<=2):
			o="almost perfect"
		else:
			o="not perfect"
		print(inp,o)



	except Exception as e:
		break