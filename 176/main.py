def decimal_place(a, b, n):
    # 计算 a/b 的小数部分
    decimal_part = a / b - a // b
    
    # 将小数部分乘以 10 的 n 次方，然后取整，再对 10 取余，得到第 n 位小数
    digit = (decimal_part * 10 ** n) % 10
    
    return int(digit)

# 读取输入的整数
a, b, n = map(int, input().split())

# 调用函数计算并打印结果
print(decimal_place(a, b, n))
