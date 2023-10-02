
largest = 0;


smallest =float('inf');


number_inputs = int(input("Enter the number of values you want : "))


for digit in range(number_inputs):
    number = float(input("Enter a number: "))


    if number > largest:
        largest = number


    if number < smallest:
        smallest = number


print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")








