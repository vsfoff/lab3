def fac(number):
    f = 1
    for i in range(1, number + 1):
        f *= i
    return f


while True:
    number = int(input())
    operation = input()
    if operation == "+":
        print(number + int(input()))
    elif operation == "-":
        print(number - int(input()))
    elif operation == "*":
        print(number * int(input()))
    elif operation == "/":
        print(number // int(input()))
    elif operation == "%":
        print(number % int(input()))
    elif operation == "!":
        print(fac(number))
    else:
        break
