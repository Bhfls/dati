# BEGIN: 7ycj1j394bfi
def is_light_on(times):
    return times % 2 == 1

M = int(input())
if 1 < M < 100:
    result = is_light_on(M)
    print(int(result))

# END: 7ycj1j394bfi
