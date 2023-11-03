score=[[25,50,75]
       ,[40,50,60],
       [75,65,80]]

average=[]

for num in score:

    num_average =sum(num)/len(num)
    average.append(num_average)

    all_average=sum(average)/len(average)


print(f'the average is :{average}')
print(f'the total average is : {all_average}')
