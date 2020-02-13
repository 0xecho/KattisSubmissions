inp = input().split()
print(inp[1] if inp[0]==1 else (int(inp[0])*(int(inp[1])-1))+1 )