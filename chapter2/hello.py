# from string import ascii_letters
# import random
#

import re

print("True" if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', '2FeTo') else "false")

contact='Eddie Esther,Home:0802-694-0144,work:0803-444-0144'
re.findall(r"\d{4}-\d{3}-\d{4}",contact)
print(contact)

for phone in re.finditer(r"\d{3}-\d{3}-\d{4}",contact):
    print(phone.group())


learn=[2,2,1,1,5]
m=0
for i in learn:
    if (learn.count(i)%2!=0):

    # if (learn.count(i)==1):
        m=i
        break
print(m)
# print single number out when you have duplicate number






# x=3
# y=2
# num=lambda x , y : x * y
# print(num(3,2))

# number = int (input("enter the length of password: "))
# s="abcdefghijklmnopqrstuvwxyz?.><,_)(*&^%$#@!"
# p="".join(random.sample(s,number))
# print(p)
# generating random password



#
# x=1
# while x <= 10:
#     if x % 3 == 0:
#         print(x)
#     x+=1
    # divisible by 3 using loop
# The above code is a simple Python while loop that iterates through the numbers from 1 to 10 and prints the values that are divisible by 3.




# l=[1,2,3,4,5]
# for i in l[::-1]:
#     print(i,end=" ")
#
# # reverse of a list
#
#
#
# list_i=[2,3,4,5,6]
# list_i.append(1)
# list_i.insert(7,0)
# print(list_i)
# list_i.sort()
# print(list_i)
#
# csv_data = "kay,27,earnest"
# you_i=csv_data.split(",")
# print(you_i)
#
# x = [[1,2,3],[4,5,6],[7,8,9]]
# for y in zip(*x):
#     print(y,end=" ")
#
#
#
#
# def func(x, y = None):
#     if y is None:
#         y=[1]
#     y.extend(x)
#     return y
# print(func([0],[2,4,5]))
#
# l = ['a','b','c','d']
# res ="".join(l)
# print(res)
#
#
#
#
#
#
#
# item1=['x']
# item1.extend(['yz'])
# print(item1)






s="  ismail  "
s= s.strip()
print(s.capitalize())
print(s.upper())
print(s.lower())
print(''.join(["a","b","c","d","e"]))
print(s.count( "i"))
# count the occurance of word in string
print(s.index("i"))
# check index of character
print (ord ("i"))

# check ascii number
print(ord("I"))

if s.startswith("i"):
    print("you will make it more bigger inshal Allah ismail ")



def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"

text = "This is awesome"
word = "awesome"

print(search(text,word))

one = [13, 45 , 44]
two = [23, 66, 34]
all= one + two
print(all,min(one),max(two))




def func(x):

  res = 0

  for i in range(x):

     res += i

  return res

print(func(3))



x = 365
y = 7
# this is a comment

print(x % y)

def sum(x):
    res = 0

    for i in range(x):
        res += i

    return res


print(sum(4))

def double(a, b):
  return [a*2, b*2]

x = double(6, 9)
print(x)


def max(x, y):
  if x >=y:
    return x
  else:
    return y

if max(6, 4) > 10:
  print("Yes")
else:
  print("Nope")

def foo(x, y):

  if x >= y:

    return x

  else:

    return y

x = foo(4, 7)

print(x)



def msg(num, ch):

  print(ch+str(num))

msg(18, 'A')





from calendar import*
year = int (input('Enter year: '))
print(calendar(year,2,1,8,3))





def print_sum_twice(x, y):
  print(x + y)
  print(x + y)

print_sum_twice(5, 8)

def exclamation(word):
  print(word + "!")

exclamation("spam")
exclamation("eggs")
exclamation("python")


def print_double(x):

   print(2 * x)

print_double(3)

def foo():

   print(1)

   print(2)



foo()

foo()

txt = "hello"

print(max(txt))

print("This is a sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())





x = "Hello ME"
print(x.replace("ME", "world"))






str = "some text goes here"
x = str.split(' ')
print(x)



x = ", ".join(["spam", "eggs", "ham"])
print(x)




a = "{x}, {y}".format(x=5, y=12)
print(a)


print("{0}{1}{0}".format("abra", "cad"))

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)





nums = [2,4,8,9,5]


nums.insert(1, 3)

nums.remove(9)

nums.insert(0, nums.count(8))

print(nums[3])





list = [8, 4, 2, 6]

list.remove(2)

print(len(list)+list.count(6))






x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)






nums = [1, 3, 5, 2, 4]

res = min(nums) + max(nums)

print(res)


x = [2, 4, 5, 7, 4]

y = x.index(4)

print(y)


letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))







nums = [9, 8, 7, 6, 5]

nums.append(4)

nums.insert(2, 11)

print(len(nums))





words = ["Python", "fun"]
words.insert(1, "is")
print(words)




nums = [1, 2, 3]
nums.append(4)
print(nums)



x ="abc"

x *= 2

print(len(x))



letters = ["a", "b", "c"]

letters += ["d"]

print(len(letters))

out_list=[1,2,3]
out_list.insert(1,4)
print(out_list)





y_list = [2,4,6,8,10]
g=y_list.copy()
result= [x*2 for x in y_list if x%3 ==0]

print(g,result)

n=[76,24]
p = n.copy()
n.pop()

print(p, n)



x,y=2,10
x*=(y*x+1)
print(x)


print("some text")


print(str(12))

for i in range(10,20,3):



    print (i , end = " ")





lis ="string girls"


for m in   lis:

    result =tuple(lis)


print(result, end = " ")












lis=[1,2,3,4,5,6]
for m in lis:
    print(m)

    if m >= 4:

        break






my_lists = [1,2,3,4]
second_list = [5,6,7,8,9]
third_list = [10,11,12,13,14,15]
for x in second_list,third_list:
    my_lists.append(x)
print(my_lists)


sum =0

#your code goes here
for a in range(1 , 101):

    sum =sum + a
print(sum)



N = int(input("enter number:"))
sum =0
#your code goes here
for i in range(1,N+1):
    sum =sum + i
print(sum)

x = [6, 4, 2, 9]

x = x[::-1]

print(x[0]+x[2])







for i in range(10):

  if not i % 2 == 0:

    print(i+1)



list = [1, 1, 2, 3, 5, 8, 13]

print(list[list[4]])

res="names"
# why is this printing an
print(res[1::-1])


nums = [5, 42, 7, 1, 0]
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.
res = nums[::-1]
print(res)

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# question to ask on this .....why is this output [49,36]
print(sqs[7:5:-1])



squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])




squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])






squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])


for x in range(5):
    print("Hello!")

x = list(range(7, 3, -1))
print(x)




numbers = list(range (3,15,3))
print(numbers)

numbers = list(range(5,20,2))
print(numbers)


numbers = list(range(3,8))
print(numbers)





numbers = list(range(10))
print(numbers)




for i in range(0,5):
    print(i)


nums = [1, 2, 3, 4]

res = 0

for x in nums:

    if x % 2 == 0:

        continue

    else:

        res += x

print(res)

list = [2, 3, 4, 5, 6, 7]

for x in list:

   if(x%2==1 and x>4):

      print(x)

      break



text = "some text"
for x in text:
  if x == 't':
    break
  print(x)




str = "testing for loops"
count = 0

for x in str:
  if x == 'o':
    count += 1
# counting the number of character that appears in a string
print(count)






nums = [4, 7, 3, 1]

for x in nums:

    print(x*2)



words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")





nums = [10, 9, 8, 7, 6, 5]

nums[0] = nums[1] - 5

if 4 in nums:

  print(nums[3])

else:

  print(nums[4])








words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)








nums = [1, 2, 3]
print(nums * 3)







x = [2, 4]

x += [6, 8]

print(x[2]//x[0])




nums = [1, 2, 3]
print(nums + [4, 5, 6])


nums = [1, 2, 3, 4, 5]

nums[3] = nums[1]

print(nums[3])







nums = [5, 8, 2]
nums[1] = 42

print(nums)




str = "Hello world!"
print(str[6])



m = [
[1, 2, 3],
[4, 5, 6]
]

print(m[1][2])

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])




weight=float(input("enter your weight in kg:" ))
height=float(input("enter your height in meters:"))


bmi=weight/(height*height)

if bmi<18.5:
    category="underweight"
elif bmi >=18.5 and bmi <25:
    category="normal"
elif bmi >=25 and bmi<30:
    category="overweight"
else:
    category="obesity"

print(bmi)
print(category)







i = 0

x = 0

while i < 4:

    x+=i

    i+=1



print(x)






d={"Africa":["congo","Nigeria"]}

d["south_america"]="brazil"
print(d)



""
while False:

  print("Looping...")

i = 0
while True:
    i += 1
    if i == 2:
        continue
    if i == 5:
        break

    print(i)

i = 5

while True:

  print(i)

  i = i - 1

  if i <= 2:

    break

x=1

while x==1:

   print("In the loop")
   x+=1



x = 0
while x <= 20:
    print(x)
    x += 2

i = 3

while i>=0:

   print(i)

   i = i - 1



sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)

x=10
while x >= 0:
    print(x)

    x -= 1



i = 1

while i <= 5:

  print(i)

  i = i + 1



if not True:

   print("1")

elif not (1 + 1 == 3):

   print("2")

else:

   print("3")





test_list=[[0,0,0],
           [0,0,0]]


for i ,val in enumerate(test_list):

    for j ,_ in enumerate(val):

        test_list[i][j]=5

print(test_list)

tuple=(1,2,[3,4],(5),{6,7,8})
print(tuple[3])




x = 10

y = 20

if x > y:

   print(x+y)

else:

   print(y-x)




num = 3
if num == 1:
  print("One")
else:
  if num == 2:
    print("Two")
  else:
    if num == 3:
      print("Three")
    else:
      print("Something else")

if 1 + 1 == 2:

   if 2 * 2 == 8:

      print("if")

   else:

      print("else")

x = 4
if x == 5:
   print("Yes")
else:
   print("No")




x = 'a'
if x < 'c':
    x += 'b'
if x > 'z':
    x += 'c'

print(x)


num = 7

if num > 3:

   print("3")

   if num < 5:

      print("5")

      if num ==7:

         print("7")

spam = 7

if spam > 5:

   print("five")

if spam > 8:

   print("eight")





bill = float(input("enter amount"))
tip=bill*20/100
print(f'the tip is :{tip}')

x = 3

num = 17

print(num % x)

x = 5

y = x + 3

y = int(str(y) + "2")

print(y)


# that will output 82

age = int(input("enter a number"))

print(age+8)
#

spam = "7"

spam = spam + "0"

eggs = int(spam) + 3

print(float(eggs))

my_list=[]
for row in range(2):

    for column in range(3):
        my_list.append(row*column)
        print(f'[{column}][{row}]={row*column}', end = ' ')
    print()
print(my_list)




# numbers=list(range(1,21))
# # def even(n):
# #     return n%2==0
# # result=list(filter(even,numbers))
# result=list(filter(lambda n:n%2==0,numbers))
# print(result)

# numbers=list(range(1,11))
# numbers2=list(range(1,11))
# print(list(zip(numbers,numbers2)))

# letters=list(ascii_letters)
# print(letters)


print(random.choice([1,2,3,4,5]))



tuple1=1,2,3,4,5,6,7,8,9,10
w,x,y , *other=tuple1
print(x,y,w)

String = 'hello world'
result = String.split(" ", 0)
print(result, end = " ")


print(2.71)
print("October")

print("28"+"6")


print("balance:",5000)

print("Iron", "Man", sep ="-")

year = 2023
print(year + 5)

x = 8
print(x)
x = 41
print(x)

age = 42
age = 24
print(age)

x = 9
y = 5

print(x*y)
print(x/y)




result = 798
currency = "$"
print("Total:", currency, result)


a = 2
b = 4
print(a+b)

numbers=[]
for i in range(1,11):
    numbers.append(i)
print(numbers)




numbers2=list(range(1,11))
print(numbers2)

# print list from 1 to 10

def even_check(n):
    ans = 0
    if n % 2 == 0:
        ans = n
    return ans


even_list=filter(even_check,numbers2)
print(list(even_list))
# check and print out even number in a list

result=[i for i in range(1,11)if i % 2 == 0]
print(result)


def my_sort(numbers2:list):
    for i in range (len(numbers2)):
        for j in range (i+1):
            if numbers2[j]< numbers[i]:
                numbers2[i] ,numbers2[j]=numbers2[j],numbers2[i]
    return numbers2
print(my_sort(numbers2))

x = 9.34

y = int(x)

print(y)


age = 42
print("His age is " + str(age))



a = 5

b = 9

x = str(a)

y = str(b)

print(x+y)

a,b,*c,d = [1,2,3,4,5,6,7]
print(c)


width = input("enter width")

height = input("enter height")

area = int(width) * int(height)

print(area-9)


x = 2
print(x)

x += 3
print(x)



x = 8

x -= 2
print(x)

x /= 3
print(x)

x **= 5
print(x)


x = 9

x %= 2


x+=3
print(x)

x = "spam"
print(x)

x += "eggs"
print(x)

x = "a"

x *= 3

print(x)

a = 8
a -= 1
a += 2

print(a)

miles = int(input())
km = miles * 1.60934

print(km)

