#progrsm to check lesp year or not 
yy=int(input())
if (yy%4==0):
    print("yes")
elif(yy%400==0):
    print("yes")
elif(yy%100==0):
    print("no")
else:
    print("no")
