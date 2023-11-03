
# sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
# def split_list_to_half():
#     split=5
#     first_half=sample_input[:split]
#     second_half=sample_input[split:]
#     return first_half,second_half
# print(split_list_to_half())
#
# sample_input = ['','ABC','xyz', '', 'abc', 'XYZ']
#
# def remove_string():
#     for item in sample_input:
#         if item== '':
#
#             sample_input.remove(item)
#     return sample_input


# input1 = ['a', 'b', 'c' ,'d', 'e']
# input2 = [1, 2, 3, 4, 5]
# def two_list_dictionary(input1, input2):
#
#     return dict(zip(input1,input2))
# print(two_list_dictionary(input1,input2))



# sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
#
# def findinglargestsmallest(sample_list):
#     largest=sample_list[0]
#     smallest=sample_list[0]
#     for num in sample_list:
#         if num > largest:
#             largest=num
#
#     for num in sample_list:
#         if num < smallest:
#             smallest=num
#     return largest-smallest
#
#
#
# print(findinglargestsmallest(sample_list))
points = 35
points = 45
print(points)

sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]

def remove_list_func(sample_input):
    new_list = []
    for num in sample_input:
        if num not in new_list: new_list.append(num)
    d1=new_list[:4]
    d1.pop(2)

    return d1
print(remove_list_func(sample_input))