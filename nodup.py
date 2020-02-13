import sys
T = input().split()

for i in T:
	if T.count(i)>1:
		print("no")
		sys.exit()
print("yes")
