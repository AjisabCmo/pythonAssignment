number =int (input ("enter a number:"))

digit1 = number // 10000
digit2 = number // 1000 %10
digit3 = number // 100 % 10
digit4 = number //  10 % 10
digit5 = number % 10

print(f"{digit1:> 4} {digit2:> 4} {digit3:> 4} {digit4:> 4} {digit5:> 4}")