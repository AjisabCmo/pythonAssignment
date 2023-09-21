deposit = int(input ("enter the amount of investment :"))



for i in range(1,31):
    roi = deposit * 10/100
    new_investment = deposit + roi
    deposit=new_investment
    print(f" your roi is  ${roi:.2f} ,your investment is now  $ {new_investment} ,in year ,{i}")
