a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
d=int(input("enter d="))
if a>b and a>c and a>d:
    print("a is max")
elif b>c and b>d:
    print("b is max")
elif c>d:
    print("c is max")
else:
    print("d is max")
