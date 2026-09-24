def calculate(a, b):
    if operation == "+":
        return (a+b)
    elif operation == "-":
        return (a-b)
    elif operation == "*":
        return (a*b)
    elif operation == "/":
        return (a/b)
    else:
        return ("invalid opperation!")


try:
    a = int(input("enter first number: "))
    b = int(input("enter second nubmber: "))
    operation = input("enter operations(+,-,*,/): ")
    print(calculate(a, b))
except:
    print("please enter valid nubmbers only")
