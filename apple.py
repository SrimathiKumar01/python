ayt=["Sri","sindhu","kishore"]
for q in ayt:
    print(q)

for i in "Sindhu":
    print(i)


apple=["red","green","yellow"]
for i in apple:
    print(i)
    if i=="green":
        break

num=20
for i in range(2,num+1,2):
    print(i)


num=10
for i in range(2,num-1,2):
    print(i)

sum=0
n=10
for i in range(2,n+1,2):
    sum=sum+i
print(sum)



sum=0
num=20
for i in range(1,num+1):
 sum=sum+i
print(sum)

 


print("Hello" + " "+ input("What is your name:"))



def fact(n):
   if(n==0):
       return 1
   else:
       return fact(n-1)*n
