input()

x = [int(i)for i in input().split()]

y = [i for i in x if x.count(i)==1]
if not y:
	print("none")
else:
	print(x.index(max(y))+1)