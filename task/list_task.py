number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result= []
for num in number:
    if num % 2 == 1:
        result.append(num*2)
        result[1:8]=[0]*len(number[1:8])
print(result)
