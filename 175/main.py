def last_three_digits(a, b):
    result = 1
    for _ in range(b):
        result = (result * a) % 1000
    return result

a, b = map(int, input().split())
print(f"{last_three_digits(a, b):03}")
