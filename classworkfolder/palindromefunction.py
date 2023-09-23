def palindrome(number):

    numbers =number
    reverse=0
    while number !=0:
        remainder=number%10
        reverse =reverse * 10 + remainder
        number=number//10

    if numbers==reverse:

        return True
    else:
        return False


print(palindrome(12121))


# num = 20022
# tempo = num
# revers = 0
# while num != 0:
#     result1 = num % 10
#     print(result1)

    # revers = revers * 10 + result1
    # tempo /= 10

    # if revers == tempo:
    #     return pali
    #
    # else:
    #     return pali



#
# result = makepalindrome(2002)
# print(result)
