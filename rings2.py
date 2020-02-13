import sys
n,m = [int(i)for i in input().split()]

l=[]

l.append("0"*(m+2))
for _ in range(n):
	l.append("0"+input().replace("T","1")+"0")
l.append("0"*(m+2))
changed = True
mx = 0
for i in range(len(l)):
	l[i] = list(l[i])

while changed:
	changed = False
	for i in range(1,n+1):
		for j in range(1,m+1):
			if l[i][j]=="." or l[i-1][j]=="." or l[i+1][j]=="." or l[i][j+1]=="." or l[i][j-1]==".":
				continue
			if not int(l[i][j]):
				continue
			
			if min(int(l[i-1][j]),int(l[i][j-1]),int(l[i+1][j]),int(l[i][j+1]))==int(l[i][j]):
				# l[i] = l[i][:j]+str(max(min(int(l[i-1][j]),int(l[i][j-1]),int(l[i+1][j]),int(l[i][j])),int(l[i][j+1])))+l[i][j+1:]
				l[i][j] = str(max(int(l[i][j])+1,min(int(l[i-1][j]),int(l[i][j-1]),int(l[i+1][j]),int(l[i][j]),int(l[i][j+1]))))

				mx=max(mx,int(l[i][j]))

				
				# print(i,j)
				changed=True
	# sys.exit()
		
ds = 3 if mx>=10 else 2
for i in l[1:-1]:
	for j in i[1:-1]:
		print("."*(ds-len(j))+j,end="")
	print()
	

