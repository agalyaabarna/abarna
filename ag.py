A1,B2,C3=input().split()
if (A1 > B2) and (A1 > C3):
   largest = A1
elif (B2 > A1) and (B2 > C3):
   largest = B2
else:
   largest = C3
 
print('',largest)
