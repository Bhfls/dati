# BEGIN: 9ycj0r9hxj4e
n = int(input())
ages = []
for i in range(n):
    age = int(input())
    ages.append(age)
average_age = sum(ages) / n
print(f"{average_age:.2f}")
# END: 9ycj0r9hxj4e
