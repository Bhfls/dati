def find_pattern(numbers):
    diff = numbers[1] - numbers[0]
    ratio = numbers[1] / numbers[0]
    if all(numbers[i+1] - numbers[i] == diff for i in range(1, len(numbers)-1)):
        return numbers[-1] + diff
    elif all(numbers[i+1] / numbers[i] == ratio for i in range(1, len(numbers)-1)):
        return numbers[-1] * ratio
    else:
        return None

# 读取输入
t = int(input())
for _ in range(t):
    numbers = list(map(int, input().split()))
    next_number = find_pattern(numbers)
    if next_number is not None:
        numbers.append(next_number)
    print(*numbers)
