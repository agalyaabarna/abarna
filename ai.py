#a
num1 = int(input())
if num1 > 1:
    for j in range(2, num1):
        if (num1 % j) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
