import sys

l = [[]]
lc= 0

for line in sys.stdin:
	line = line.strip()
	if line == "":
		l.append([])
		lc+=1
	else:
		l[lc].append(line)

def srt(x):
	return x[::-1]
for i in l:
	i.sort(key=srt)
for i in l:
	m = len(max(i,key=len))

	for j in i:

		print(" "*(m-len(j)),j,sep="")
	if not i==l[-1]:
		print()

