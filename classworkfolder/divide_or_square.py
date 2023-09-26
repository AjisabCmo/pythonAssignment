def divide_or_square(number):
    numbers=number**0.50

    if number%5==0:
        return numbers

    #else:
    if number%5!=0:
        return numbers

solution =(divide_or_square(10))
print(f'{solution:.2f}')
