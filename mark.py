mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
averagemark=(mark1+mark2+mark3+mark4+mark5)%5
if(averagemark<35):
    print("Additional class should be required")
else:
    print("Your are good to go")

