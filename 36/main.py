num = int(input())
num = (num % 10) * 10 + num // 10
if num == 3:
    print("03")
else:
    print(num)
