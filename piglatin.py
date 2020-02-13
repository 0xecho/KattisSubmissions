while 1:

	try:

		x = input().split()

		for i in x:
			if i[0] in ["a","e","i","o","u","y"]:
				print(i+"yay",end=" ")
			else:
				while not i[0] in ["a","e","i","o","u","y"]:
					 i = i[1:]+i[0]
				print(i+"ay",end=" ")
		print()
	except:
		break