#a
M,N=map(int,input().split())
for j in range(M,N):
  sum=0
  temp1=j
  while(temp1>0):
    L=temp1%10
    sum=sum+L**3
    temp1=temp1//10
  if(j==sum):
    print(sum,end=" ")
