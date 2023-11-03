

def reverse_tuple(num):



    num_list = list(num)


    num_list.reverse()


    reversed_tup = tuple(num_list)

    return reversed_tup

tuple1 = (10, 20, 30, 40, 50)
reversed_tuple1 = reverse_tuple(tuple1)
print(reversed_tuple1)
