l = int(input("enter the number "))
c = int(input("enter the number "))
for i in range(1, l+1):
    for j in range(1,c+1):
        if i == 1 or i == l or j == 1 or j == c:
            print("*",end ="")
        else:
            print(" ",end ="")

    print()

     