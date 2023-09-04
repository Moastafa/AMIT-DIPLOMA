def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def sub(*args):
    result = args[0]
    for i in args[1:]:
        result -= i
    return result

def multi(*args):
    result = 1
    for i in args:
        result *= i
    return result

def div(*args):
    result = args[0]
    for i in args[1:]:
        result /= i
    return result

def calculator():
    '''' this function take the any count of numbers and the command of mathematical operation 
    and return the result , ask the user if there is an another operatin .
    note: this function is in an mo'''
    command = input("Enter a command (add, sub, multi, div): ")
    nums = input("Enter the numbers (space separated): ").split()
    nums = list(map(int, nums))
    print (nums)
    
    if command == "add":
        result = add(*nums)
    elif command == "sub":
        result = sub(*nums)
    elif command == "multi":
        result = multi(*nums)
    elif command == "div":
        result = div(*nums)
    else:
        print("Invalid command")
        return

    print("The result is:", result)

    again = input("Do you want to make another operation? (continue/stop): ")
    if again.lower() == "continue":
        calculator()
    else:
        print("Thank you for using the calculator")
calculator()