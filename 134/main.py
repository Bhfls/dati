# 判断年份是否由两组相同的数字组成
year = input()

if year[0] == year[2] and year[1] == year[3]:
    print("YES")
else:
    print("NO")