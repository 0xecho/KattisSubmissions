n = int(input())

tv = input().split()

cmd = input().split()

cmd = [(tv[ord(i)-65] if i.isalpha() else i) for i in cmd]

stack = []

idx = 0
try:
		
	while 1:
		while cmd[idx].isalpha():
			stack.append(cmd[idx])
			idx+=1
		op = cmd[idx]
		idx += 1 
		# print(cmd,stack,op,idx)

		if op=="*":
			op1 = stack.pop()
			op2 = stack.pop()
			if op1 == "T" and op2 == "T":
				stack.append("T")
			else:
				stack.append("F")

		elif op=="+":
			op1 = stack.pop()
			op2 = stack.pop()
			if op1 == "T" or op2 == "T":
				stack.append("T")
			else:
				stack.append("F")
		else:
			stack.append("T" if stack.pop()=="F" else "F")
		# print(cmd)
		# print(stack)
		# print(op)
		if idx > len(cmd)-1:
			break	

	print(*stack)
except :
	print("T")