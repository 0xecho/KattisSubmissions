a = sum([int(i)for i in input().split()])
b = sum([int(i)for i in input().split()])
if a==b:
    print("tie")
else:
    print("Gunnar" if a>b else "Emma"  )