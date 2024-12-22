n = int(input())
students = set(range(1, n + 1))
for _ in range(n - 1):
    students.remove(int(input()))
print(students.pop())
