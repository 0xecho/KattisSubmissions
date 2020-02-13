inp=[int(i) for i in input().split()]


if inp[1]+inp[2]==inp[0]:
    print(str(inp[0])+"="+str(inp[1])+"+"+str(inp[2]))
elif inp[1]-inp[2]==inp[0]:
    print(str(inp[0])+"="+str(inp[1])+"-"+str(inp[2]))
elif inp[1]/inp[2]==inp[0]:
    print(str(inp[0])+"="+str(inp[1])+"/"+str(inp[2]))
elif inp[1]*inp[2]==inp[0]:
    print(str(inp[0])+"="+str(inp[1])+"*"+str(inp[2]))


elif inp[1]+inp[0]==inp[2]:
    print(str(inp[0])+"+"+str(inp[1])+"="+str(inp[2]))
elif inp[0]-inp[1]==inp[2]:
    print(str(inp[0])+"-"+str(inp[1])+"="+str(inp[2]))
elif inp[0]/inp[1]==inp[2]:
    print(str(inp[0])+"/"+str(inp[1])+"="+str(inp[2]))
elif inp[1]*inp[0]==inp[2]:
    print(str(inp[0])+"*"+str(inp[1])+"="+str(inp[2]))
