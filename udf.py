#sum(n a n r)
def fun():
    a=10
    b=20
    c=a+b;
    print("sum=",c)
fun()

#sum(w a n r)
def fun(a,b):
    c=a+b;
    print("sum=",c)
fun(10,20)

#sum(n a w r)
def fun():
    a=10
    b=20
    c=a+b;
    return c
ans=fun()
print("sum=",ans)

#sum(w a w r)
def fun(a,b):
    c=a+b;
    return c
sum=fun(10,20)
print("sum=",ans)



#.armstrong(w a n r)
def arm(a):
    i=a
    s=0
    while(i>0):
        digit=i%10
        s=s+(digit*digit*digit)
        i=i//10
    if s==a:
        print("armstrong")
    else:

        print("not armstrong")
            
n=int(input("enter number:"))
arm(n)

#.prime(w a w r)
def pri(i):
    prime=0
    for j in range(1,i+1):
        if i%j==0:
            prime+=1
    if prime==2:
        print(i,end="\t")
        return prime
print("1 to 62 prime number")
for i in range(1,62):
    ans=pri(i)

#.palidrom(n a n r)
def pal():
    s=int(input("enter number:"))
    temp=s
    rev=0

    while s>0:
        digit=s%10
        rev=rev*10+digit
        s=s//10
    if rev==temp:
        print("palidrom")
    else:
        print("not palidrome")
pal()




























    



























