x = input()

while len(x)%4:
	x = "0"+x
o=""
for i in range(len(x)//4):
	t=str(hex(int(x[4*i:4*i+4],8))[2:])
	o+="0"*(3-len(t))
	o+=t
while len(o) and o[0]=="0":
	o=o[1:]
print(o.upper() if len(o)else 0)