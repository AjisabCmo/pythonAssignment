




my_list =[[2,4,5,6],[2,3,5,6]]

def sum_list(my_list):
    total = 0
    for num in my_list:
        total += sum(num)
    #     sum collect iterables
    return total
print(sum_list(my_list))


a,b=my_list
result = sum(a) + sum(b)
print(result)



