def calculator():
    print("Select the operation")
    print("press 1 for addition")
    print("press 2 for subtraction")
    print("press 3 for multiplication")
    print("press 4 for division")

    operation=input("select he operation type:")
    num1=float(input("Enter your first value ="))
    num2=float(input("Enter your second value ="))


    if operation=="1":
        print(f"{num1+num2}")
    elif operation=="2":
        print(f"{num1-num2}")
    elif operation == "3":
        print(f"{num1*num2}")
    elif operation == "4":
        print(f"{num1/num2}")
    else:
        raise ValueError("invalid input")
    return
calculator()


