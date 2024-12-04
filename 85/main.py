num1, num2, num3 = map(float, input().split())
max_num = max(num1, num2, num3)
if max_num.is_integer():
    max_num_str = str(max_num).rstrip('0').rstrip('.')
    print(max_num_str)
else:
    print(max_num)