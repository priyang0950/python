num=int(input("enter num:"))
i=1
sum=0
while i<=num:
    if i%2==1:
        print(i)
    sum+=i
    i+=2

print("sum odd num=",sum)
