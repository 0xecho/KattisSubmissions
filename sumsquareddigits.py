def tb(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

T = int(input())
for i in range(T):
	K,b,n=[int(i) for i in input().split()]
	print(K,sum(i*i for i in tb(n,b)))