n=int(input("Enter no to print="))
for i in range(2,n):
    prime=0
    for j in range(2,i):
        if i%j==0:
            prime+=1
    if prime:
        print(i)
