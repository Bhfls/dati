a, b = map(float, input().split())
r = a - int(a / b) * b
print(f"{r:.2f}")
