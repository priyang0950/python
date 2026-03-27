a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
if a<b:
    if a<c:
        print("a is main")
    else:
        print("a is min")
else:
     if b<c:
         print("b is min")
     else:
         print("c is min")
