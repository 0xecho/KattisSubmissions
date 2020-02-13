inp = input().split()
print(max([int(i[::-1]) for i in inp]))