weight, is_urgent = input().split()
weight = int(weight)

if weight <= 1000:
    postage = 8
elif weight % 500 == 0:
    postage = 8 + (weight - 1000) // 500 * 4
else:
    postage = 8 + (weight - 1000) // 500 * 4 + 4

if is_urgent == 'y':
    postage += 5

print(postage)
