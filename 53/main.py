num = int(input())
bai = num // 100
ge = num % 10
shi = num // 10 % 10
new_num = ge * 100 + shi * 10 + bai
print(new_num)
