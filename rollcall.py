x=[]
while 1:
	try:
		x.append(input().split())
	except:
		break
ln = {}
fn = {}
for i in x:
	if i[1] in ln:
		ln[i[1]]+=1
	else:
		ln[i[1]]=1
	if i[0] in fn:
		fn[i[0]]+=1
	else:
		fn[i[0]]=1

x=sorted(sorted(x),key=lambda a:a[1])

for i in x:
	print(i[0],end=" ")
	print("" if fn[i[0]]==1 else i[1])

# print(x,ln,fn,sep="\n")