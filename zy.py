a,b=map(int,input().split())
c=[]
for j in range(a+1,b+1):
	if(j%2!=0):
	 c.append(j)  
	print(*c,sep=" ")
