chinese, math = map(int, input().split())
if (chinese <= 60 and math >= 60) or (chinese >= 60 and math <= 60):
    print(1)
else:
    print(0)