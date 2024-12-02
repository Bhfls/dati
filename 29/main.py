def area(b, h):
    return 0.5 * b * h

base, height = map(float, input().split())

s = area(base, height)
s = int(s)
print(f"s={s}")
