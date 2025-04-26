n=5
for row in range (1,n+5):
    for col in range (1,n+1):
        if row==n or col==1 or col==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()