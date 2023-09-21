p=int(input("enter the principal amount:"))
r=int(input("enter the annual rate:"))
# n=int (input("enter the number of year:"))
rValue = r / 100
a = (rValue+1)
a10 = a ** 10
a2 = p * a10

a20=a**20
a3=p * a20

a30 =a**30
a4=p* a30

print(a2 , a3 , a4)