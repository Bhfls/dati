

def find_initial_money(total_money):
    # 计算每人最后的金额
    final_amount = total_money / 3 

    # 逆向推理，计算初始的钱数
    a = final_amount
    b = final_amount
    c = final_amount
    a /= 2
    b /= 2
    c = c + b + a 
    a /= 2
    c /= 2
    b = a + b + c
    b /= 2
    c /= 2
    a = a + b + c
    # 通过逆向推理，计算初始的钱数 
    
    return a, b, c 
# 输入总钱数 
total_money = int(input("请输入总钱数: ")) 
a, b, c = find_initial_money(total_money) 
if a.is_integer() :
    print(int(a), end=' ')
else:
    print(a, end=' ')
if b.is_integer() :
    print(int(b), end=' ')
else:
    print(b, end=' ')
if c.is_integer() :
    print(int(c))
else:
    print(c)
