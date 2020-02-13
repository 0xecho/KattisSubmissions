input()

l= sorted([int(i)for i in input().split()])[::-1]

x =[]

for i in range(len(l)):
    x.append(l[i]+i+1)

print(max(x)+1)
