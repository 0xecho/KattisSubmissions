inp=[int(i)for i in input().split()]

p=inp[0]*3+inp[1]*2+inp[2]
m={
	8:"Province or ",
	5:"Duchy or ",
	2:"Estate or ",
	0:"",
}
n={
	6:"Gold",
	3:"Silver",
	0:"Copper",
}
c=0
for i in m:
	if i<=p:
		c=max(c,i)
d=0
for i in n:
	if i<=p:
		d=max(d,i)
print(m[c],n[d],sep='')