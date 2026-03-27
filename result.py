s1=int(input("enter sub 1 mark="))
s2=int(input("enter sub 2 mark="))
s3=int(input("enter sub 3 mark="))
s4=int(input("enter sub 4 mark="))
s5=int(input("enter sub 5 mark="))

total=s1+s2+s3+s4+s5
print("total=",total)
per=total/5
print("per=",per)

if s1<s2 and s1<s3 and s1<s4 and s1<s5:
    print("s1 is min")
elif s2<s3 and s2<s4 and s2<s5:
    print("s2 is min")
elif s3<s4 and s3<s5:
    print("s3 is min")
elif s4<s5:
    print("s4 is min")
else:
    print("s5 is min")
    
if s1>s2 and s1>s3 and s1>s4 and s1>s5:
    print("s1 is max")
elif s2>s3 and s2>s4 and s2>s5:
    print("s2 is max")
elif s3>s4 and s3>s5:
    print("s3 is max")
elif s4>s5:
    print("s4 is max")
else:
    print("s5 is max")

if per>90:
    print("grade=A+")
elif per>80:
    print("grade=A")
elif per>70:
    print("grade=B+")
elif per>60:
    print("grade=B")
elif per>45:
    print("grade=c")

cnt=0
if s1<35:
    cnt+=1
if s2<35:
    cnt+=1
if s3<35:
    cnt+=1
if s4<35:
    cnt+=1
if s5<35:
    cnt+=1
    
if cnt==0:
    print("result=PASS")
elif cnt>=1 and cnt<=2:
    print("result=ATKT")
else:
    print("result=FAIL")
        
    
