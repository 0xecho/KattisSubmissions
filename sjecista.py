import math
x=int(input())
print(int((math.factorial(x)/(12*math.factorial(x-4)))/2) if not x is 3 else 0)