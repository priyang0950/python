a=[1,2,3,4,5,6,7]
print(a)
position=int(input("Enter position="))
n=len(a)
if position<1 or position > n:
    print("invalid position")
else:
    for i in range(position,n):
        a[i-1]=a[i]
    del a[n-1]
    print("upload list",a)
        
