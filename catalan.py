from decimal import *
import sys
x=5500
sys.setrecursionlimit(x)

l=[0]*5010
l[0]=1
l[1]=1

getcontext().prec = 5001

def c(n):
	for i in range(2,n+1):
		l[i]= (Decimal((4*i-2))/Decimal(i+1))*l[i-1]
		# print(((2*(2*i-1))//(i+1)),l[i-1],l[i])
	return l[n]
c(5000)
for i in range(int(input())):
	print(round(l[int(input())]))
# print(l[:20])