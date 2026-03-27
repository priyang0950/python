num=int(input("enter no:"))
count=0
while num!=0:
    if num<0:
        num=-num    
    num=int(num/10)
    count+=1

print("count no=",count)
