r,c= [int(i)for i in input().split()]

if r==c:
	print("0.000000000")
else:
	print("%.7f"%((((r-c)**2)/((r)**2))*100))
