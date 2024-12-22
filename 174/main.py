# BEGIN: 9ycx48j43m4
n = int(input("请输入一个正整数："))
if n < 1 or n > 20:
    print("输入的数不符合要求，请输入一个1到20之间的正整数。")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("{factorial}")
# END: 9ycx48j43m4
