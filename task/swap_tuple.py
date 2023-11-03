# tuple3 = (15, 25, 60, 50, 30, 40, 45, 55)
# num = list(tuple3)
# num[0],num [7]=num[7],num[0]
# new_tuple3=tuple(num)
# print(new_tuple3)



def swap_first_and_last_elements(tuple3):
    num = list(tuple3)
    num[0], num[7] = num[7], num[0]
    new_tuple3 = tuple(num)
    return new_tuple3


tuple3 = (15, 25, 60, 50, 30, 40, 45, 55)
new_tuple3 = swap_first_and_last_elements(tuple3)
print(new_tuple3)