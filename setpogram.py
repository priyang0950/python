#1.
primeset=set()
for n in range(2,101):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        primeset.add(n)
print("prime num set",primeset)

#2.
s=(1,1,1,2,3,4,4,2,1,1)
s1=set(s)
for i in s1:
    count=0
    for j in s:
        if i==j:
            count+=1
print("count:",count)

#3.
s={1,2,3,4,5,6,7}
s1=set(s)
s.remove(2)
print(s)

#4.
s={1,2,3,4,5,6,7,8,9}
s1=set()
for i in s:
    s1.add(i*i)
print(s1)

#5.
s={10,20,30,6,13,17,27}
for i in s:
    num= int(i)
    if num%2==0:
        print("even num:",num)

#6.
s="hello"
for i in s:
    s1=set(s)
print(s1)

#7.
s={1,2,3,4,5,6,7,8}
s1=set()
for i in s:
    if i%2==0:
        s1.add(i)
print(s1)


#8.
s={10,20,30,3,4}
large=max(s)
print(large)


















