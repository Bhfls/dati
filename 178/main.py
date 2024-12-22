# BEGIN: 9oefxaz14wxr
def calculate_last_two_digits(n):
    # 计算1992的n次幂
    result = pow(1992, n)
    # 将结果转换为字符串，并取最后两位
    last_two_digits = str(result)[-2:]
    return last_two_digits

# 读取输入的n值
n = int(input())

# 调用函数计算并打印结果
print(calculate_last_two_digits(n))
# END: 9oefxaz14wxr
