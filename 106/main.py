height, weight = map(int, input().split())

standard_weight = (height - 100) * 0.9

if weight > standard_weight * 1.1:
    print("fat")
elif weight < standard_weight * 0.9:
    print("thin")
else:
    print("standard")
