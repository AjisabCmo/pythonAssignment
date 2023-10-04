numbers=[15,20,25,20,10,5]
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest=num
print(smallest)