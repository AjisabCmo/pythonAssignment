numbers=[15,20,25,20,10,5]
largest=numbers[0]
for num in numbers:
    if num > largest:
        largest=num
print(largest)