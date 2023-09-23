picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

for number in picture:
    for digit in number:
        if digit==0:
            print(' ' ,end=' ')
        else:
            print('*' , end= ' ')


    print()


#0 to display ' ' and 1 to display   '*'