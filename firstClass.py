#first_name ='Ajiboye'
import random

#second_name ='ismail'

#full_name = first_name + ' ' + second_name

#print(full_name)
#password = input("enter a password:")

#hidden_password =len(password )* '*'
#print(hidden_password)

#num1=float('1')
#num2=2
#print(num1 + num2)
#print(2+3*4/2**4)

#message1 = 'hello'
#message2 = 'welcome'
#message3 = 'xplorers'

#print(message1+' ' + message2+' ' + message3)
#long_string = """
           #   abdullahi is a boy and he is smart and sharp
             # speccial belated birthday shout out to his
         #     mom .God in his mercy continue to bless her
         #     and give her more joy ,guide and protect her.
       #       more life in good health and wealth my wife
          #    i love you dearly .."""
#msg = f'{message1 + " how are you"}\n{message2}\n{message3}'
#print(msg)

#print(long_string)

age = int(input("Enter an age:"))
if age < 18:
    print("you are not eligible to enter our club..")
else:
    print("eligible")

result ="not eligible" if age < 18 else "eligible"
print(result)

language = input("Enter your language: ")
match language:
    case "yoruba":
        print("welcome to ibadan")
    case "igbo":
        print("welcome to anambra")
    case "hausa":
        print("welcome to kano")
    case _:
        print("you're not from here")

score = int(input("enter your score:"))
result= ""
if score>70:
    if score>90: #nested if is whats happening here
        result="pass with distinctions"
else:
    result="fail"

print(result)

if score >= 90 and score <= 100:
    result ="distinction"
elif 80 <= score < 90:
    result ="excellent"
elif score >= 70 and score < 80:
    result= "B grade"
elif score >= 60 and score < 70:
    result ="c grade"
elif score >= 50 and score < 60:
    result ="d grade"
elif socre < 50:
    result= "fail,come back next time"
print(result)

print (f'your score is {score} and your result is {result}')# you are formatting your string which is (score and result)

print(bool(0)) #if the program language see it ,it will be false
print(bool(5))
print(bool(''))# false empty string
print(bool('fhjsj'))


name = input ("enter your name: ")
if name:
    print(f"your name is {name}")
else:
    print("no name entered")

    count =0
    while count <10:
        print(random.randint(1, 21))#infinite loop
        count +=1#with this it will not run to infinite  and it will make it false and stop run when it is false

_ismail =random.randint(1, 21)
print(_ismail)
#if age >=18 and age <=65:
  #  print("you are eligible to enter our club")
#if age > 65:
   # print("Stay home...")


# list in python

my_playlist = []
names =["arua","joy","qudus","ope"]
names2=list("isreal","abbey","mando")