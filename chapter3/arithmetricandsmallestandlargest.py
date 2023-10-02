number=int(input("enter a number:"))
sum =number
product=number
smallest = number
largest = number
count =0
for count in range (1,4):
    number= int(input("enter a number  : "))
    count += 1
    sum+=number
    product*=number
    average = sum / count




    if number < smallest:
        smallest = number
    if number > largest:
        largest = number





print(f"Sum: {sum}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")



