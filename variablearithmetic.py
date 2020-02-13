inp  = input()
m={}
for i in range(101):
	m[str(i)] = i
while inp!="0":

	if "+" in inp:
		x=inp.split(" + ")
		sx = []
		s = 0

		for i in x:
			if i in m:
				s+=m[i]
		if s:
			sx.append(str(s))
		for i in x:
			if not i in m:
				sx.append(i)
		print(" + ".join(sx) if sx else 0)

	elif "=" in inp:
		x=inp.split(" = ")

		m[x[0]] = int(x[1])
	else:
		print(m[inp] if inp in m else inp)

	inp=input()