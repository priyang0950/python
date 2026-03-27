#2.
str="priyang kachhadiya"
print("upper case=",str.upper())
print("lower case=",str.lower())


#10.
str="priyang"
rev=""
for i in str:
    rev=i+rev
print(rev)


#3.
str="kachhadiya priyang"
count=len(str.split())
print("count num of word=",count)


#4.
str=input("enter string=")
str2=input("replace elment=")

ans=str.replace(" ",str2)
print(ans)


#14.
str="priyang kachhadiya"
word=str.split()
long=""
for w in word:
    if len(w)>len(long):
        long=w
print("long word=",long)


#1.
p=input("enter to cheak num=")

if p==p[::-1]:
    print("palidrom")
else:
    print("not palidrome")


#8.
p=input("enter string=")
space=p.replace("","")
print("replace white space:",space)

#5.
str=input("enter string:")
count=0
for _ in str:
    count+=1
print("length of the string",count)


#11.
str="hello word"
words=str.split()
for i in range(len(words)):
    print(words[i].capitalize(),end=" ")

#13.
str="priyang kachhadiya"
str2=str.split()
print(str2)


#9.
str=input("enter string:")
vowels="aeiouAEIOU"
cout=0
for i in str:
    if i in vowels:
        cout+=1
print("vowels num count=",cout)


#7.
str=input("enter name:")
str2=str.swapcase()
rev=""
for i in str2:
    rev=i+rev
print("swapedcase:",str2)

print("rev swapedcase:",rev)


#6.
str=input("enter string:")
punctuation="!@#$%^&*()[]"
ans=""
for i in str:
    if i not in punctuation:
        ans+=i
print("remove punctution=",ans)


#12.
str=input("enter string:")
p=0
ans=""
for i in str:
    count=str.count(i)
    if count>p:
        p=count
        ans=i
print("frequent character=",ans)








 
        



    











