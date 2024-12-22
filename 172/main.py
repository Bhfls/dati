n = int(input())
total_cost = 0
for i in range(n):
    words = int(input())
    if words <= 70:
        total_cost += 0.1
    else:
        total_cost += (words // 70 + 1) * 0.1
print(f"{total_cost:.1f}")
