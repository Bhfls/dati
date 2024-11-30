# 简易的计算器
num1, num2, op =  input().split()

num1 = int(num1)
num2 = int(num2)

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)  
elif op == "/":
    if num2 == 0:
        print("Divided by zero!")
    else:
        print(num1 / num2)
else:
    print("Invalid operator!")