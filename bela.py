DOM={}
NDOM={}
DOM["A"]=11
NDOM["A"]=11
DOM["K"]=4
NDOM["K"]=4
DOM["Q"]=3
NDOM["Q"]=3
DOM["J"]=20
NDOM["J"]=2
DOM["T"]=10
NDOM["T"]=10
DOM["9"]=14
NDOM["9"]=0
DOM["8"]=0
NDOM["8"]=0
DOM["7"]=0
NDOM["7"]=0

inp,B = input().split()
score = 0
for i in range(4*int(inp)):
	c,s=list(input())
	if s==B:
		score += DOM[c]
	else:
		score += NDOM[c]
print(score)
