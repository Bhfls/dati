def round_half_even(number, digits):
    # 将数字乘以 10 的指定次幂，以便进行四舍五入
    rounded_number = round(number * (10 ** digits)) / (10 ** digits)
    return rounded_number

# 输入浮点数和小数位数
f, d = map(float, input().split())

# 调用函数进行四舍五入
rounded_f = round_half_even(f, d)

# 输出结果
print(rounded_f)
