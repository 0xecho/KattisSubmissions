import string
T=int(input())
while T:
	inp=input().lower()
	f=[]
	for i in string.ascii_lowercase:
		if not i in inp:
			f.append(i)
	if len(f)==0:print("pangram")
	else: print("missing","".join([i.lower() for i in sorted(f)]))
	T-=1