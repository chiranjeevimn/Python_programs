r=int(input("enter the row"))
R=2*r-2
for i in range(0,r):
    for j in range(0,R):
        print(end=" ")
    R=R-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()


