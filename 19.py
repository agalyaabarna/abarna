#a
A=int(input())
sum=1
if(A==0):
    print("1")
else:
    for j in range(1,A+1):
        sum=sum*j 
    print(sum)
