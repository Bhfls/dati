def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_e(n):
    e = 1
    for i in range(1, n + 1):
        e += 1 / factorial(i)
    return e

n = int(input())

result = calculate_e(n)
print(f"{result:.10f}")
