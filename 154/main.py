# BEGIN: 9ycx9j44389
n = int(input())
numbers = list(map(int, input().split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print(even_sum)
# END: 9ycx9j44389
