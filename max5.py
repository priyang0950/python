a=int(input("enter value a="))
b=int(input("enter value b="))
c=int(input("enter value c="))
d=int(input("enter value d="))
e=int(input("enter value e="))
if a>b and a>c and a>d and a>e:
    print("a is max")
elif b>c and b>d and b>e:
    print("b is max")
elif c>d and c>e:
    print("c is max")
elif d>e:
    print("d is max")
else:
    print("e is max")
