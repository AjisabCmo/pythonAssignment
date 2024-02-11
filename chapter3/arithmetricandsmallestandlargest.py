# number=int(input("enter a number:"))
# sum =number
# product=number
# smallest = number
# largest = number
# count =0
# for count in range (1,4):
#     number= int(input("enter a number  : "))
#     count += 1
#     sum+=number
#     product*=number
#     average = sum / count
#
#
#
#
#     if number < smallest:
#         smallest = number
#     if number > largest:
#         largest = number
#
#
#
#
#
# print(f"Sum: {sum}")
# print(f"Average: {average}")
# print(f"Product: {product}")
# print(f"Smallest: {smallest}")
# print(f"Largest: {largest}")



sum = 0
product = 1
largest = 0
user=4
smallest = user
for i in range (user):
    print("input value ",(i+1)," :" ,end = " ")
    user = int (input())
    sum += user
    product *= user
    average = sum /user
    if user > largest:
        largest = user
    if user < smallest:
        smallest = user




print("the sum is :",sum)
print("the product is :",product)
print("the average is :",average)
print("the largest is :",largest)
print("the smallest is ",smallest)


