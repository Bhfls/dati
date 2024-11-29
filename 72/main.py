# BEGIN: 5ycj9s9j4f5e
num = list(map(int, input().split()))
for i in range(5):
    num[i] = num[i] // 3
    if i == 0:
        num[4] += num[i]
        num[1] += num[i]
    elif i == 1:
        num[0] += num[i]
        num[2] += num[i]
    elif i == 2:
        num[1] += num[i]
        num[3] += num[i]
    elif i == 3:
        num[2] += num[i]
        num[4] += num[i]
    elif i == 4:
        num[3] += num[i]
        num[0] += num[i]
print(*num)
# END: 5ycj9s9j4f5e
