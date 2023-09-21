#index = 0
#
#while index < 10:
    #score = int(input("enter student score :"))
   # total += score
  ##  index += 1
#average =total /index
#print(f"the total of scores by the student is {total} the average score is {average}")




#index = 0
#total = 0

#while index < 10:
    #score = int(input("enter student score :"))
    #total += score
   # index += 1
#average =total /index
#print(f"the total of scores by the student is {total} the average score is {average}")




total=0
count=0
score = int(input("enter student score or -1 to stop"))
while score!= -1:
    total += score
    count+= 1
    score = int(input("enter student score or -1 to stop"))
average = total / count
print(f"{average:.2f}")

