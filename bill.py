unit=float(input("enter unit="))

pri=float
if unit<=50:
    pri=50*0.50
elif unit<=150:
    pri=50*0.50+unit-50*0.75
elif unit<=250:
    pri=50*0.50+100*0.75+unit-150*1.20
elif unit<=350:
    pri=50*0.50+100*0.75+100*1.20+unit-250*1.50
elif unit>=350:
    pri=50*0.50+100*0.75+100*1.20+100*1.50+unit-350*2
    
bill=float
bill=pri
print("bill=pri",bill)

gst=float
gst=pri*0.18
print("gst=",gst)

total=float
total=pri+gst
print("total bill=",total)
