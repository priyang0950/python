num=int(input("enter num="))
sum=0
same=num
while num!=0:
    digit=num%10
    sum=sum+digit
    num=int(num/10)

print("sum=",sum)
