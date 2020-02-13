def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

a,b,c = [int(i)for i in input().split()]

print("yes" if lcm(a,b)<=c else "no")