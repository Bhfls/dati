# BEGIN: 9ycj3x449j34
m, n = map(int, input().split())
sum = 0
for i in range(m, n+1):
    if i % 2 == 1:
        sum += i
print(sum)
# END: 9ycj3x449j34
