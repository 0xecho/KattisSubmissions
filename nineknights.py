g=[list(input())for i in range(5)]
d = [
	(2,1),
	(2,-1),
	(1,2),
	(1,-2),
	(-2,1),
	(-2,-1),
	(-1,2),
	(-1,-2),
]
valid=1
count = 0
for i in range(5):
	for j in range(5):
		if not g[i][j]=="k":
			continue
		count+=1
		for k,l in d:
			pos = []
			if i+k>=0 and i+k<5:
				if j+l>=0 and j+l<5:
					pos.append([i+k,j+l])

			for x in pos:
				if g[x[0]][x[1]]=="k":
					valid=0
					# print(x)
if not count==9:
	valid  =0 
print("valid" if valid else "invalid")