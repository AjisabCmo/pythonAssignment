sum_of_natural_number=0

for number in range (1,11):
    sum_of_natural_number +=number

print("the sum of the first 10 natural number:" , sum_of_natural_number)


count =1
sum = 0
while count <=10:
    sum =sum +count
    print(sum , end = " ")
    count+=1