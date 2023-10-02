
passes=0
failures=0



while True:
    try:
        numbers=int(input("enter number"))
        if numbers == -1:
            break
        elif numbers== 1:
            passes +=1
        elif numbers == 2:
            failures += 1
        else:

             print("wrong input,please enter 1 for pass or 2 for fail")
    except ValueError:
        print("wrong input,please enter 1 for pass or 2 for fail")

total_tests=passes+failures
print(f"total tests:{total_tests}")
print(f"passes: {passes}")
print(f"failures:{failures}")


