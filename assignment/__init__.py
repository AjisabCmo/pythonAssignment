



def list_to_dictionary(sample_input):
    d1 = {}
    for count in sample_input:
        result=count[0]
        d1[result]=count

    # d1=dict(enumerate(sample_input))
    return d1


def list_to_dic_same(param):
    d1={}
    for count in param:
        result=count[0]
        if result in d1:
            result=count[0].upper()

        d1[result]=count
    return d1


def two_list_dictionary(input1, input2):

    return dict(zip(input1,input2))
# The zip function takes two or more iterable sequences and combines them element-wise into tuples.

# the dict constructor is then used to convert these pairs of elements into a dictionary.
def largestsmallestlist(sample_list):
    largest = sample_list[0]
    smallest = sample_list[0]

    for num in sample_list:
        if num > largest:
            largest = num
    for num in sample_list:
        if num < smallest:
            smallest = num

    return largest-smallest


def frequency_greater_than_value_func(sample_input):
    new_list = []
    for num in sample_input:
        if num not in new_list: new_list.append(num)
        d1 = new_list[:4]
    d1.pop(2)
    return d1
