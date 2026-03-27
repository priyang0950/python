l=[1,2,3,2,4,5,3]
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
print("unique element",l1)
