# file = open("demo.txt", mode="w")
# file.write("ope is a short girl\n")
# file.write("Abdullahi is a smart Boy\n")
# file.close()


# with open("demo.txt", mode="w") as file:
#     file.write("ope is a short girl\n")
#     file.write("Abdullahi is a smart Boy\n")
#     file.write("i love you Dad\n")
# #
# with open("demo txt", mode ="a") as file:
#     file.write(" and i also love you mum")

# mando = " "
# with open('demo.txt', mode='r') as file:
#     for record in file:
#         mando+=record
#         print(mando)


# with open('demo.txt', mode='r') as file:
#     for record in file:
#         account,name,*balance = record.split()
#         print(f'{account:<10}{name:<10}{balance}')

# try:
#     with open('demo.txt', mode = 'r') as datas:
#         for data in datas:
#             a, *b = data.split()
#             print(a, *b)
# except FileNotFoundError:
#     print("make sure you check your file spelling")
#
# try:
#     age = int(input("Enter ya age:"))
#     result=age/10
#     print(result)
# except ZeroDivisionError:
#     pass
# except ValueError:
#     print("ur age cannot be string literal")
# finally :
#     print("finally block runs either there is exception")
# finally will run if there is exception or not

# def age_check(n):
#     if n <= 0 :
#         raise ValueError("age cannot be less than or equal to zero")
#     return f'your age is {n} years old'
# print(age_check(-2))



class Point:
    color = "blue"
    # this is the class  instance attribute
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def draw(self):
        print(f"drawing from point {self.a} to point {self.b}..")

    def __str__(self):
        return f"Point({self.a}{self.b})"


Point.color = "red"
point1 = Point(1,2)
point2 = Point(5,5)
print(point1.color)
point1.a=3
# change a to 3 and dont modify your attribute outside the class
point1.draw()
point2.draw()
#  def __init__(self):
#     # no args constructor
#     self.a = 1
#     self.b = 2
#
#
#  def draw(self):
#     print(f"drawing from point {self.a} to point {self.b}..")
#
#
# point1 = Point()
# point2 = Point()
#
# point1.draw()
# point2.draw()

