x, n = map(int, input().split())
y = 1
for i in range(n):
    y = (y + x / y) / 2
print("%.3f" % y)
