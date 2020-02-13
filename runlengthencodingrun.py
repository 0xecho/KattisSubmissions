c,s = input().split()
o=''
cnt=0
p=''
if c=="E":
	for i in s+"~":
		if cnt==0:
			p=i
			cnt+=1
		elif not i==p:
			o+=p+str(cnt)
			cnt=1
			p=i
		else:
			cnt+=1
else:
	for i in range(0,len(s),2):
		print(s[i]*int(s[i+1]),end="")
print(o)