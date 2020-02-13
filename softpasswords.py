s = input()
p = input()

v=0

if s==p:
	v=1
if s[0].isdigit() and s[1:]==p:
	v=1
if s[-1].isdigit() and s[:-1]==p:
	v=1
ip = "".join([i.lower() if i.isupper() else i.upper() for i in p])
if s==ip:
	v=1

print("Yes"if v else"No")
