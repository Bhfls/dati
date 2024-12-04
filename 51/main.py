import decimal
decimal.getcontext().prec = 50  # 设置精度为50位
a, b = map(decimal.Decimal, input().split())
r = a
while r > b:
    r -= b
print(r)
# 解决减法尾数溢出问题



