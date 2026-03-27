#1.find duplicates
l=[1,2,3,4,2,5,6,7,3,4,8,8]
dup=[]
for i in l:
    if l.count(i)>1 and i not in dup:
        dup.append(i)
print("duplicate=",dup)


#2.find missing number in a list

l=[1,2,3,4,6,7,8,9]
n=len(l)+1
missing=(n*(n+1))//2-sum(l)
print("mising num=",missing )

