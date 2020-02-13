a,b= [int(i)for i in input().split()]
c,d= [int(i)for i in input().split()]
e,f= [int(i)for i in input().split()]

ta = a*b+c*d+e*f

yes=0
x=0
for i in range(1,500):
	if ta == i*i:
		x=i
		yes=1
		break
if not yes:
	print("NO")
else:
	if (a+c == x or a+e == x or c + e ==x or a+c+e==x or a==x or c==x or e==x) and (b+d == x or b+f == x or d + f ==x or b+d+f==x or b==x or d==x or f==x):
		print("YES")
	else:
		print("NO")