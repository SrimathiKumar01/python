Salary=int(input("salary:"))
age=int(input("age:"))
if(Salary>=20000 or age<=25):
    loan=int(input("loan:"))
    if(loan<=50000):
        print("Maximum ")
    else:
        print("Maximum loan amount is 50000")
else:
    print("Your are not Eligible")