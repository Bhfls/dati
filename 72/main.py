# BEGIN: 9p4j3934k34
# n = int(input())
nums = list(map(int, input().split()))
n = len(nums)
for i in range(n):
    nums[i] //= 3
    if i == 0:
        nums[n - 1] += nums[i]
        nums[i + 1] += nums[i]
    elif i == n - 1:
        nums[i - 1] += nums[i]
        nums[0] += nums[i]
    else:
        nums[i - 1] += nums[i]
        nums[i + 1] += nums[i]

for num in nums:
    print('{:5d}'.format(num), end='')
# END: 9p4j3934k34
