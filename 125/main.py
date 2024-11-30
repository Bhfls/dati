def calculate_postage(weight):
    if weight <= 0 or weight > 100:
        return "Fail"
    elif weight <= 10:
        rate = 0.80
    elif weight <= 20:
        rate = 0.75
    elif weight <= 30:
        rate = 0.70
    else:
        return "Fail"
    
    postage = weight * rate + 0.2
    return f"{postage:.2f}"

# 测试代码
weight = float(input())
print(calculate_postage(weight))
