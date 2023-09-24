
def fizz_buzz():
    number = 1
    while number <= 50:
        if number % 5 == 0 and number % 3 == 0:

            print('fizzbuzz')
        else:

            if number % 3 == 0:
                print('fizz')
            else:
                if number % 5 == 0:
                    print('buzz')
                else:
                    print(number)
        number += 1

print(fizz_buzz())













# number = 1
# while number <= 50:
#     if number % 5 == 0 and number %3==0:
#
#         print('fizzbuzz')
#     else:
#
#         if number % 3== 0:
#             print('fizz')
#         else:
#             if number % 5==0:
#                 print('buzz')
#             else:
#                 print(number)
#     number+=1

# for l in range(3):
#     print(end='')
#     for i in range(10):
#         print('\n',end=' \t')
#         for j in range(i):
#             print("*",end=' ')



