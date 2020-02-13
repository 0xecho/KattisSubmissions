for _ in range(int(input())):
    name = input()
    address = input()
    n=int(address.split()[0])
    m={
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
    }
    while n:
        # print(n)
        cmd = input()

        if not cmd[0]=="+":
            for i in str(cmd):
                m[int(i)]+=1
            n-=1
        else:
            cmd=cmd.split()
            for i in range(int(cmd[1]),int(cmd[2])+int(cmd[3]),int(cmd[3])):
                for j in str(i):
                    m[int(j)]+=1
                n-=1
        s=0
        for i in m:
            s+=m[i]
    print(name)
    print(address)
    for i in m:
        print("Make {} digit {}".format(m[i],i))
    print("In total {} digit".format(s) if s==1 else "In total {} digits".format(s))