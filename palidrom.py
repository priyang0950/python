num=int(input("enter num="))
rev=0
same=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=int(num/10)
    
if same==rev:
    print("num is palidrom")
else:
    print("num is not palidrom")
    
print("rev num=",rev)
