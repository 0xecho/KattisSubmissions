inp = [int(i) for i in input().split()]
f = {}
for i in range(1,inp[0]+1):
	for j in range(1,inp[1]+1):
		if i+j in f.keys():
			f[i+j] += 1
		else:
			f[i+j] = 0
m=max(f.values())
for i in f:
	if f[i]==m:
		print(i)