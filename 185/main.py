# BEGIN: 5ycj4j9d04rq
N = int(input())
odd_count = 0
even_count = 0

for i in range(N):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count, even_count)
# END: 5ycj4j9d04rq
