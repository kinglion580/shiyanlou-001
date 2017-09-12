monthMoney=int(input("please input money"))
ds=3500
payable=monthMoney-ds
single=0
if payable<1500:
    single=payable*0.03-0
elif payable>=1500 and payable<4500:
     single=payable*0.1-105
elif payable>=4500 and payable<9000:
     single=payable*0.2-555
elif payable>=9000 and payable<35000:
     single=payable*0.25-1005
elif payable>=35000 and payable<55000:
     single=payable*0.3-2002
elif payable>=55000 and payable<80000:
     single=payable*0.35-5505
elif payable>=80000:
     single=payable*0.45-13505
if single<0:
    single=0
#print "%.2f" %single  
print('{:.2f}'.format(single))

