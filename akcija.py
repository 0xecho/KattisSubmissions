l=[]
for _ in range(int(input())):
	l+=[int(input())]
l.sort(reverse=True)
s=0
for i in range(int(len(l))):
	if (i+1)%3==0:
		continue
	s+=l[i]
print(s)
