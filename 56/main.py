# BEGIN: 9ycx9j149wxr
def find_nth_term(a1, a2, n):
    common_difference = a2 - a1
    nth_term = a1 + (n - 1) * common_difference
    return nth_term

a1, a2, n = map(int, input().split())
result = find_nth_term(a1, a2, n)
print(result)
# END: 9ycx9j149wxr
