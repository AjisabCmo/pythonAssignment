
sum =0
product=1
smallest = float('inf')
largest = float('-inf')
count =0
while (count<4):
    number= int(input(f"Enter the {count} of values  : "))

    sum+=number
    product*=number
    average = sum / 4




    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

    count += 1



print(f"Sum: {sum}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")



