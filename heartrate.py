T = int(input())
for _ in range(T):
	b,p=[float(i)for i in input().split()]
	BPM=60*b/p
	LABPM=BPM-BPM/b
	HABPM=BPM+BPM/b
	print(LABPM,BPM,HABPM)
