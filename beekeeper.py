import sys
vow = ["a","e","i","o","u","y"]
pos = []
for i in vow:
	pos.append(i+i)
for line in sys.stdin:
	m={}
	if not int(line):
		break
	for _ in range(int(line)):

		x=input()
		m[x] = sum([x.count(i) for i in pos if i in x])

	print(max(m,key=lambda x:m[x]))
	# print(m)