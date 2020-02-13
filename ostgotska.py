inp = input()
cae = len([i for i in inp.split() if "ae" in i])
if cae/len(inp.split())>=0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
