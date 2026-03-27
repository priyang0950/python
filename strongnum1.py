def strong(num):
    
    temp=num
    s=0
    while temp>0:
        d=temp%10
        fact=1
        for i in range(1,d+1):
            fact*=i           
        s+=fact
        temp//=10
        
    return s==num

for num in range(1,1001):
    ans=strong(num)
    if ans:
        print(num)
