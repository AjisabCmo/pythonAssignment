




def unique_even(sample_list1):
    new_list = []
    even = []
    for num in sample_list1:
        if num not in new_list:
            new_list.append(num)

    for yes in range(len(new_list)):
        if new_list[yes] % 2 == 0:
            even.append(new_list[yes])

    return even
sample_list=[1,3,2,5,3,4,6,4,6,9,8,2,10,8,6,12,15,10,4,6,14]
print(unique_even(sample_list))







sample_list=[1,3,2,5,3,4,6,4,6,9,8,2,10,8,6,12,15,10,4,6,14]

def no_duplicate (n):




    return [ i for i in n if i % 2==0 ]

print(no_duplicate(sample_list))
