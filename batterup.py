T=int(input())
n=0
m=0
for i in [int(i) for i in input().split()]:
	if i!=-1:
		n+=1
		m+=i
print(m/n)