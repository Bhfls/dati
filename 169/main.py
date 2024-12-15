n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0
sum_ = 0
for i in range(n):
    if sum_ + a[i] > m:
        count += 1
        sum_ = a[i]
    else:
        sum_ += a[i]
if sum_ > 0:
    count += 1
print(count)
