T = int(input())

for _ in range(T):
	k,n = [int(i) for i in input().split()]
	print(k,int(n/2*(2+(n-1)*1)),int(n/2*(2+(n-1)*2)),int(n/2*(4+(n-1)*2)))