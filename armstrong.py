num=int(input("enter num="))
sum=0
i=num
while i>0:
    digit=i%10
    sum=sum+digit*digit*digit
    i=int(i/10)
print("num=",sum)

if sum==num:
    print("same")
else:
    print("not same")
