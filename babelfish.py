import sys
m={

}

while 1:
	inp = input()
	if inp=="":
		break
	inp = inp.split()

	m[inp[1]]=inp[0]

for line in sys.stdin:
	if line.strip() in m:
		print(m[line.strip()])
	else:
		print("eh")