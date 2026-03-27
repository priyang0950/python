num=int(input("enter any no:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
print("rev:",rev)
    
