l="Anywhere is fine I guess"
for _ in range(int(input())):
	r= int(input())
	x= input()
	m=[]
	for k in range(r):
		m.append(input())
	if "pea soup" in m and "pancakes" in m:
		l=x
		break
print(l)