n,m = [int(i)for i in input().split()]

l=[]

for i in range(n):
	l.append(list(input()))

l= [list(i) for i in zip(*l)]

print(sum([1 for i in l if i.count("_")==n])+1)
# print([i.count("_") for i in l])