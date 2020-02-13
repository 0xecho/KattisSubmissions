d={
   2:["a","b","c"],
   3:["d","e","f"],
   4:["g","h","i"],
   5:["j","k","l"],
   6:["m","n","o"],
   7:["p","q","r","s"],    
   8:["t","u","v"],
   9:["w","x","y","z"],
   0:[" "],

}
n=1
for _ in range(int(input())):
    inp = input()
    l=-1
    print(f"Case #{n}: ",end='')
    for j in inp:
        for i in d: 
            if j in d[i]:
                if i==l:
                    print(" ",end='')
                print(str(i)*(d[i].index(j)+1),end='')
                l=i
    n+=1
    print()
