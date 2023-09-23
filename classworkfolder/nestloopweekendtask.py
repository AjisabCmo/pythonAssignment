import rows as rows


def nest_pattern(rows):

    for count in range(1, rows + 1):
        for digit in range(1, rows - count + 1):
            print("", end="")
        for star in range(1, count + 1):
            print("*", end=" ")

        print()

    for count in range(rows - 1, 0, -1):
        for digit in range(1, rows - count, +1):
            print("", end="")
        for star in range(1, count + 1):
            print( "*",end=" ")

        print()
rows = 5
print(nest_pattern(rows))