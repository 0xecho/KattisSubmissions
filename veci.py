from itertools import permutations
s=input()

l=[int("".join(i)) for i in permutations(s) if int("".join(i))>int(s)]
print(min(l)if l else 0)
    
