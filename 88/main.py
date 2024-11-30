weight = float(input())
if weight <= 20:
    cost = weight * 1.68
else:
    cost = weight * 1.98
print(f"{cost:.2f}")
