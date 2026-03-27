#1.

t=("10","20","30","40","50")
largest=max(t)
smallest=min(t)
print("largest num:",largest)
print("smallest num:",smallest)


#2.
t=("10","20","30","6","13","17","27")
p=0
for i in t:
    num= int(i)
    if num%2==0:
        p+=num
print("even sum=",p)


#3.
t=(10,20,10,30,40)
p=10
count=0

for i in t:
    if i==p:
        count+=1
print("count:",count)


#4.
t=("10","20","10","30","10")
t1=()
for i in t:
    if i not in t1:
        t1+=(i,)
print("dublicate delate:",t1)

#5.
t=("10","20","30","40")
t1=("10","20","30","40")
if t==t1:
    print("both are eqval")
else:
    print("both are not eqval")

#11.
t=(10,20,30,40,50)
min=t[0]
max=t[0]
for i in t:
    if i>max:
        max=i
    if i<min:
        min=i
print("max:",max,"min:",min)
print("sum:",max+min)

#8.
t=(2,3,1,5,9,4)
sum=0
for i in range(len(t)):
    if i% 2!=0:
        sum+=t[i]
print("sum of odd index:",sum)


#7.
t=(2,3,4,5,3,7)
p=0
for i in range(len(t)):
    if t[i]>p:
        large=p
        p=t[i]
print("second large:",large)

#9.
t=(1,1,2,3,3,4,5)
p=0
for i in t:
    count=t.count(i)
    if count>p:
        p=count
        freq=i
print("freq ele:",freq)

#10.
t1=(1,2,3)
t2=(4,5,6)

t3=[]
for i in t1:
    t3.append(i)
for j in t2:
    t3.append(j)

t=tuple(t3)
print("tuple",t)

#6.
t=(1,2,3,2,1,5,4,5)
if len(t)==len(set(t)):
    print("elment are uniqe")
else:
    print("elment are not uniqe")






































    











