import math
T = int(input())
for _ in range(T):
	V,A,L,H1,H2 = [float(i) for i in input().split(" ")]
	t = L/(V*math.cos(A*3.141592653/180))
	H = V*t*math.sin(A*3.141592653/180) - 0.5*(9.81)*t*t 
	print("Safe"if H1<H-1 and H+1<H2 else"Not Safe")