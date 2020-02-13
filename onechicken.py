n,m=[int(i) for i in input().split()]
if m-n==1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif m-n==-1:
    print("Dr. Chaz needs 1 more piece of chicken!")
elif m-n<0:
    print("Dr. Chaz needs {} more pieces of chicken!".format(n-m))
elif m-n>0:
    print("Dr. Chaz will have {} pieces of chicken left over!".format(m-n))
    
