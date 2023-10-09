def add_function(numbers):
    total=0
    for num in numbers:
        total+=num

    return total


def multiply_function(numbers):
    multiply=1
    for num in numbers:
        multiply*=num
    return multiply


def largest_function(numbers):
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest


def smallest_function(numbers):
    smallest=numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def duplicate_function(numbers):
    new_list=[]
    for num in numbers:
        if num not in new_list : new_list.append(num)

    return new_list