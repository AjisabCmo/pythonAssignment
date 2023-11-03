def biggest_odd(numbers):
    return int(max([number for number in numbers if int(number) % 2 == 1]))
    # return filter(lambda n:int(n)%2==1,numbers)


