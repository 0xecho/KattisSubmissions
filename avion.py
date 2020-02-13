x = []

for i in range(5):

	if "FBI" in input():
		x.append(i+1)
if len(x):
	print(*x)
else:
	print("HE GOT AWAY!")