principal=int(input("enter principal:"))
rate=int (input("enter rate:"))
year= int (input("enter numbers of years:"))
for year in range (1,31):
    investment= principal *(1+ rate / 100)**year
    print(f"year{year},total return{investment:2f}")