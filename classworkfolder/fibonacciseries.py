# def fibonacciseries():
#         n1 = 0
#         n2 = 1
#         for number in range(2, 50):
#                 if n1 >= 50:
#                         break
#                 print(n1, end="  ")
#                 sum = n1 + n2
#                 n1 = n2
#                 n2 = sum
#         # return number
# print(fibonacciseries())





# n1 = 0
# n2 = 1
# for number in range(2,50):
#         if n1 >= 50:
#             break
#         print(n1, end="  ")
#         sum = n1 + n2
#         n1 = n2
#         n2 = sum

















def fibonacciseries(number):
        x = 0
        y = 1
        sum = x + y
        while x < number:
                print(x, end=' ')
                x = y
                y = sum
                sum = x + y



fibonacciseries(100)


# x=0
# y=1
# sum=x+y
# while x<50:
#     print(x,end=' ')
#     x=y
#     y=sum
#     sum =x + y


















