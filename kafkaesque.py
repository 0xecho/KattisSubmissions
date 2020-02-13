l = [int(input())for i in range(int(input()))]

c=1
for i in range(len(l)-1):
	if l[i]>l[i+1]:
		c+=1
print(c)