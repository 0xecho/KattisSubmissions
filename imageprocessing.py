h,w,n,m = [int(i)for i in input().split()]

g=[[int(i)for i in input().split()] for i in range(h)]
kernel=[[int(i)for i in input().split()] for i in range(n)]
fk = [[1 for i in range(m)] for i in range(n)]
for i in range(n):
	for j in range(m):
		fk[i][j] = kernel[n-i-1][m-j-1]
# print(*g,sep="\n")

fin = [[1 for i in range(w-m+1)] for i in range(h-n+1)]

for i in range(h-n+1):
	for j in range(w-m+1):
		val = 0
		for x in range(n):
			for y in range(m):
				val += g[i+x][j+y]*fk[x][y]
				# print(i,j,x,y,i+x,j+y)
		fin [i][j] = val
for i in fin:
	print(*i,sep=" ")

		