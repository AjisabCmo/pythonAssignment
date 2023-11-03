





def exercise1():
    return list(range(1,21))


def oddNumber_function(list1):
    result=[]
    for num in list1:
        if num % 2 == 1:
            result.append(num)
    return result


def doubleOddNumber(list1):
    result=[]
    for num in list1:
        if num % 2 ==1:

            result.append(num*2)
    return result





def indexfourandseventoZero(list1):
    result=[num * 2 for num in list1 if num % 2 == 1]
    result[4:8] = [0] * len(list1[4:8])
    return result


def concatenate(list1, list2):

    return [x+y for x,y in zip(list1,list2)]