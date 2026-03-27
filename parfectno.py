#parfect
num=int(input("enter num:"))
sum=0
i=1
while  i<num:
    if num%i==0:
        sum=sum+i
    i+=1
if sum==num:
    print("parfect no",num)
else:
    print("not parfect no",num)
