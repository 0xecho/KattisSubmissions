import sys
from math import factorial

for i in sys.stdin:
	i = i.strip()
	x=[factorial(i.count(j)) for j in set(i)]
	sx =1
	for _ in x:
		sx*=_

	print(factorial(len(i))//(sx))