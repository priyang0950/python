num=int(input("enter no="))
sum=0
temp=num
while temp>0:
    digit=temp%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i+=1
    sum=sum+fact
    temp=int(temp/10)

if sum==num:
    print("strong no",num)
else:
    print("not strong",num)
