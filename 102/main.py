n, x, y = map(int, input().split())
print(n - y//x - (1 if y%x else 0))
