#1. vovels remove
s="pogramming"
vovels={'a','e','i','o','u'}
ans=""
for ch in s:
    if ch not in vovels:
        ans+=ch
print(ans)


#2.
a={1,2,3,4}
b={3,4,5,6}
print(a&b)
print(a|b)
print(a-b)


#3.subset
s={10,20,30}
t={5,10,15,20,25,30}
print(s.issubset(t))

#4.
d={'a':1,'b':2,'c':3}
d['d']=4
d['b']=20
print(d)

#5.marged
d1={'a':1,'b':2}
d2={'b':3,'c':4}
marged={**d1,**d2}
print(marged)


#6.freq
words=["apple","banana","apple","pear","banana","apple"]
freq={}
for w in words:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1
print(freq)


#7.
l=[1,2,3,4,5]
d={}
for index,value in enumerate(l):
    d[value]=index
print(d)


#8.
a=[3,1,2,3,2,1]
d={}
for item in a:
    d[item]=True
ans=list(d.keys())
print(ans)

#9.
a={'red','blue','green'}
b={'blue','yellow','pink'}
c=(a-b)|(b-a)
print(c)


#10.
s={1,2,3}
s.update([4,5])
print(s)

#11.
a=[10,20,30,20,10,40]
p=set()
dup=set()
for n in a:
    if n in p:
        dup.add(n)
    else:
        p.add(n)
print(dup)

#12.
marks={'raj':50,'amit':75,'neha':65,'kiran':75}
highest=max(marks.values())
top=[]
for name,score in marks.items():
    if score==highest:
        top.append(name)    
print("highest mark:",highest)
print("toper:",top)


#13.
words=["python","java","cpp","kotlin"]
d={}
for w in words:
    d[w]=len(w)
print(d)



























































































