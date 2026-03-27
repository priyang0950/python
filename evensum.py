num=int(input("enter num:"))
i=1
sum=0
while i<=num:
    if i%2==0:
        sum+=i
        print(i)
    i+=1
    
print("sum even num=",sum)
