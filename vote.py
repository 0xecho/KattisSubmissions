import sys
for i in range(int(input())):
	x=[]
	for _ in range(int(input())):
		x.append(int(input()))

	ts = sum(x)

	if x.count(max(x))>1:
		print("no winner")
	elif max(x)/ts>0.5:
		print(f"majority winner {1+x.index(max(x))}")
	else:
		print(f"minority winner {1+x.index(max(x))}")
	