# BEGIN: 5ycj3n44j94r
num1, num2, num3 = map(float, input().split())
numbers = [num1, num2, num3]
numbers.sort()
for i in numbers:
    if i.is_integer():
        print(f"{int(i)}", end=' ')
    else:
        print(f"{i}", end=' ')
# END: 5ycj3n44j94r
