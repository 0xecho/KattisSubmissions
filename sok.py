a,b,c=[int(i)for i in input().split()]
i,j,k=[int(i)for i in input().split()]

f=min(a/i,b/j,c/k)

print(a-i*f,b-j*f,c-k*f)