import sys
while 1:
	x = input()
	ox = x
	if len(x)==1:
		print(x)
		continue

	prefx=""
	if x.startswith("LX") and x.count("X")==1 :

		prefx += "XL"
		x = x[2:]

	if x.endswith("VI"):
		x = x[:-2]+"IV"
	if x.endswith("XI"):
		x = x[:-2]+"IX"

	if ox=="LIX":
		print("XLI")
	elif ox=="LXXI":
		print("XLIX")
	else:
		print(prefx+x)
	break