while True:
	inp=[int(i) for i in input().split()]
	if inp==[0,0]:
		break
	if inp[0]+inp[1]==13:
		print("Never speak again.")
	elif inp[0]<inp[1]:
		print("Left beehind.")
	elif inp[0]>inp[1]:
		print("To the convention.")
	else:
		print("Undecided.")
