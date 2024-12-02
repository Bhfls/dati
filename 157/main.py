# BEGIN: 9ycx4j09wxr4
total = 0
count = 0
nums = list(map(int, input().split()))
while True:
    count = count + 1
    num = nums[count-1]
    if num == -1:
        break
    total += num
print(total)
# END: 9ycx4j09wxr4
