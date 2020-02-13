for _ in range(int(input())):

	r,c = [int(i)for i in input().split()]

	l = [input()[::-1]for i in range(r)]
	print("Test",_+1)
	print(*l[::-1],sep="\n")

