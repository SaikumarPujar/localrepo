n=[1,2,[3,4,5]]
l=[]
for i in n:
    if isinstance(i,list):
        l.extend(i)
    else:
        l.append(i)

print(l)
