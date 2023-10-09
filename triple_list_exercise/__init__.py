def triple_list_exercise(numbers):
    total = 1
    new_list = []

    for num in numbers:
        total = num * num
        result = total * num
        new_list.append(result)
    return new_list

