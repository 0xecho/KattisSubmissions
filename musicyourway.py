ind = input().split()
l = []
cmd= []
for _ in range(int(input())):
	l.append(input().split())
for _ in range(int(input())):
	cmd.append(input())

for i in cmd:
	print(" ".join(ind))
	l.sort(key=lambda x:x[ind.index(i)])
	print(*[" ".join(i) for i in l],sep="\n")
	if not i == cmd[-1]:
		print()
