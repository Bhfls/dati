def print_with_spaces(number):
    # 将数字转换为字符串，并使用字符串的 join 方法在每个字符之间插入空格
    print(' '.join(str(number)))

# 示例
input_number = int(input())
print_with_spaces(input_number)
