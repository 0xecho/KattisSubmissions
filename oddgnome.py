for i in range(int(input())):
    x = [int(i)for i in input().split()]
    x=x[1:]
    for i in range(1,len(x)):
    	if x[i]-x[i-1]!=1:
    		print(i+1)
    		break
        
