a,b=map(int,input().split())
a=list(map(int,input().split()))
m=sorted(l)
n=0
for j in range(0,len(m)):
	n=n+1
	if n==m:
		print(m[j])
