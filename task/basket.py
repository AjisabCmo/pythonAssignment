# basket=[]
# basket.append("shirt")
# basket.append(40)
# print(basket)
#
# basket.append("trower")
# print(basket)
# print(basket[0])
# print(basket[1])
# print(basket[2])
#
# len(basket)
# print(len(basket))
#
# basket_length=len(basket)
# print(basket_length)

#
#
# baskets = [2,1,4,3]
# count=0
#
# for value in baskets:
#
#
#
#     count+=value
#     average = count/len(baskets)
# largest=max(baskets)
# smallest=min(baskets)
#
# if value > largest:
#
#     largest=value
#     if value < smallest:
#         smallest=value
#
#
#
#
# print("The sum is :", count)
# print("the average is :",average)
# print("the largest is:",largest)
# print("the smallest is :",smallest)
# result=0
# #
# finds =[]
# result=0
#
# largest=0
# smallest=0
# for count in range (4):
#     find=int(input(f"enter a number {count+1}:"))
#     finds.append(find)
#     result += find
#     average = result / len(finds)
#
#     if find > largest:
#         largest = find
#     if find < smallest:
#         smallest=find
#
#
#
#
#
#
#
#
# print(f"the sum is :{result}")
# print(f"the average is :{average}")
# print(f"the largest is :{largest}")
# print(f"the smallest is :{smallest}")

#
# input_string = input('Enter numbers separated by space ')
# print("\n")
#
# numbers = input_string.split()
#
#
# for i in range(len(numbers)):
#
#     numbers[i] = int(numbers[i])
#
#
# print("Sum = ", sum(numbers))
# print("Average = ", sum(numbers) / len(numbers))







# def my_score(score):
#     return sum(score)/len (score)
#
# exam_scores =[]
# for count in range(10):
#
#     score = int(input("enter score:"))
#     exam_scores.append(score)
#
# print(my_score(exam_scores))




# def average_score(*scores):
#     total=0
#     for i in scores:
#         total +=i
#         return total/len(scores)

def reverse_list(num):
    return num[::-1]
number_list=[1,2,3,4]
reversed_list = reverse_list(number_list)
print(reversed_list)


def mymax(list1):

    largest=list1[0]

    for count in list1:



        if count > largest:
            largest = count
    return largest
list1 = [10, 3, 4, 8]
print(mymax(list1))



# things_i_need = ["shoes","bags","groceries"]



# additional_stuff_i_need=["clothes","skincare","make up"]
#
# things_i_need.extend(additional_stuff_i_need)
#
#
# print(things_i_need)

# extend method in list[]

#
# things_i_need.insert(1,"my_meds")
#
# print(things_i_need)


# insert method in list[]

#
# things_i_need.remove("shoes")
#
# print(things_i_need)


# .remove method in list[]

# popped_list = things_i_need.pop()
#
# print(things_i_need)


# pop method remove or delete number in arrangment of number and specify the number you are deleting and if you dont put number in the last item in the list bracelet [] it will delete the third number




#
# things_i_need=things_i_need.clear()
# print(things_i_need)


# clear method in list ..it will clear all the item in the list





# shoes_index=things_i_need.index("shoes")
#
#
# bag_index=things_i_need.index("bags")
#
#
# print("index of 'shoes' : ", shoes_index)
#
# print("index of 'bags' : ", bag_index)




# the index will tell you where your items are in the list[]



# shoes_count=things_i_need.count("shoes")
#
#
# bag_count=things_i_need.count("bags")
#
#
# print("Number of 'shoes' : ", shoes_count)
#
# print("Number of 'bags' : ", bag_count)



#  count will tell you how many occurence the item in the list occur



# things_i_need = [1,2,3,4,5,6,]
#
# things_i_need.reverse()
#
# print(things_i_need)


# to reverse the item in a list[]




# copied_list=things_i_need.copy()
#
# print(copied_list)


# copied all the item in the list []


def myis():

    numbers=[1, 2, 3, 4, 5]

    print(numbers[2:])

myis()

def youis():
    my_list=["joy", 23, 100,'m', 5.5]

    print(len(my_list))
youis()

letters=list('abcdefghij')
print(letters)
