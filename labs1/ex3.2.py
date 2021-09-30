input1 = float(input("введите первое число: "))
input2 = float(input("введите второе число: "))
oper = input("операция над числами: ")

if input2 == 0 and oper == "/":
    print(888888)
elif oper == "-":
    print(input1 - input2)
elif oper == "+":
    print(input1 + input2)
elif oper == "*":
    print(input1 * input2)
elif input2 != 0 and oper == "/":
    print(input1 / input2)
else:
    print(888888)
