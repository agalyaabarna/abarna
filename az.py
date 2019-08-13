A,B=map(int,input().split())
while A<B:
	for j in range(2,A):
		if A==2:
			print(2)
		if A%j==0:
			flag=0
			break
		else:
			flag=1
	if flag==1:
		print(A)
	A=A+1
