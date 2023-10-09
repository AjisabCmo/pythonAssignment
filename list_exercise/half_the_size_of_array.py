def my_life():
    my_list=['A','M','C','W','I','T']
    first_list= my_list[0::3]
    second_list=my_list[1::3]
    third_list=my_list[2::3]
    solution=first_list+second_list+third_list
    return solution
print(my_life())


