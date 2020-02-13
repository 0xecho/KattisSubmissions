l={
	"upper":0,
	"middle":1,
	"lower":2,

}
for _ in range(int(input())):

	mn = {}


	for _ in range(int(input())):

		nm,cls = input().split(":")
		cls = cls[1:-6]
		cls = cls.split('-')
		cls = "".join(map(str,list(map(l.get,cls))[::-1]))
		cls += "1"*(10-len(cls))
		if not cls in mn:
			mn[cls] = [nm]
		else:
			mn[cls].append(nm)
			mn[cls].sort()
		#print(mn)

	for i in sorted(mn):
		print(*mn[i],sep="\n")
	print("="*30)


