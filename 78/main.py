x, a, y, b = map(float, input().split())
z = (b*y - a*x) / (b - a)
print(f"{z:.2f}")
