numbers=[15,20,25,20,10,5]
new_list=[]
for num in numbers:
    if num not in new_list: new_list.append(num)
print(new_list)