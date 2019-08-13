a,b=map(int,input().split())
while a<b:
	for j in range(2,a):
		if a==2:
			print(2)
		if a%j==0:
			flag=0
			break
		else:
			flag=1
	if flag==1:
		print(a)
	a=a+1
