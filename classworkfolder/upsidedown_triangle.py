num=5
for count in range(1,num+1):
    for digit in range (count -1):
        print (' ',end='')
    for digit in range(2*(num-count)+1):
        print("*",end='')
    print()