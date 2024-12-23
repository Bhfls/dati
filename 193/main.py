def sdjhg(x, y):
    max_num = 1000
    for i in range(max_num, 0, -1):
        if i % x != 0 and i % y != 0:
            return i
    return -1

x, y = map(int, input().split())
result = sdjhg(x, y)
print(result)
