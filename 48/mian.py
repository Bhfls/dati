def calculate_original_money(x):
    # 计算甲、乙、丙原有的钱数
    # 甲 = 乙 = 丙 = x/4
    return x/4, x/2, x/4

# 输入总钱数
total_money = int(input())

# 计算并输出原有的钱数
original_money = calculate_original_money(total_money)
print("甲、乙、丙原有的钱数分别为：", original_money)
