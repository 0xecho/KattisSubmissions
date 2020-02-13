inp = input().split()
while not inp == ["0","0","0","0"]:
    p1 = sorted([inp[0],inp[1]],reverse=True)
    p2 = sorted([inp[2],inp[3]],reverse=True)
    
    p1w = False
    p2w = False

    if p1 == ["2","1"]:
        if not p2 == ["2","1"]:
            p1w = True
    elif p2 == ["2","1"]:
        p2w = True
    elif p1[0]==p1[1]:
        if p2[0]==p2[1]:
            if p1[1]>p2[1]:
                p1w = True
            elif p2[1]>p1[1]:
                p2w = True
        else:
            p1w = True
    elif p2[0]==p2[1]:
        p2w = True
    elif ''.join(p1) > ''.join(p2):
        p1w = True
    elif ''.join(p1) < ''.join(p2):
        p2w = True
    if p1w == p2w:
        print("Tie.")
    elif p1w:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")




    inp=input().split()


