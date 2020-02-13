a=input()
b=input()

nz = len(b)-1
dp = len(a)-nz


if len(b)>len(a):

	o = '0.'+"0"*(len(b)-len(a)-1)+a

else:
	o = a[:dp]+'.'+a[dp:]
x=len(o)
for i in o[::-1]:
	if not i=='0':
		break
	x-=1

o=o[:x]

if(o[-1]=='.'):o=o[:-1]

print(o)


#  120/1000 0.12