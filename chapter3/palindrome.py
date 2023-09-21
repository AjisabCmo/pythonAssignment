print("enter your number")
number =int (input())
temp =number
reverse=0

while( number >0):
    remainder=number%10

    number=number//10
    reverse = reverse * 10 + remainder
if temp ==reverse:
    print("it is a palindrome")
else:
    print("it is not a palindrome")