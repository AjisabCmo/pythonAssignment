def your_salary():
    teacher = input("Enter your name :")
    number_of_periods = int(input("enter number of period : "))

    if number_of_periods > 100:
        gross_salary = 100 * 20 + (number_of_periods - 100) * 25
    return f"Teacher: {teacher}\n Periods: {number_of_periods}\nGross salary: {gross_salary}"


print(your_salary())
