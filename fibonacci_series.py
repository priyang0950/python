#class,object.(fibonacci series)
class first:

    def __init__(self,n):
        print("con call")
        self.n=n

    def getdata(self):
        print("fibonacci series")
        a=0
        b=1
        print(a,b)
        for i in range(self.n):
            c=a+b
            print(c)
            a=b
            b=c
            print()
            
    def setdata(self):
        print("setdata is call")

n=int(input("enter num:"))
f=first(n)
f.getdata()
f.setdata()
