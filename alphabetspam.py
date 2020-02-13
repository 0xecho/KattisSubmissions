import string
inp = input()
a,b,c,d,e=0,0,0,0,len(inp)

for i in inp:
	if i=="_":
		a+=1
	elif i in string.ascii_lowercase :
		b+=1
	elif i in string.ascii_uppercase:
		c+=1
	else:
		d+=1
print(a/e,b/e,c/e,d/e,sep="\n")