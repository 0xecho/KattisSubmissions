import sys
l=[]
d=[]
for i in sys.stdin:
	l+=i.split()
for i in l:
	for j in l:
		if i==j:
			continue
		if not i+j in d:
			d.append(i+j)
		if not j+i in d:
			d.append(j+i)

print("\n".join(sorted(d)))

