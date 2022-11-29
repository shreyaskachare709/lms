n=8
for i in range(n):
    for j in range(i,n):
        if j==i or i==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



    n=7
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()