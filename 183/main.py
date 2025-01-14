n = int(input())
cocktail_cases, cocktail_effective = map(int, input().split())
cocktail_effectiveness = cocktail_effective / cocktail_cases

for _ in range(n - 1):
    cases, effective = map(int, input().split())
    effectiveness = effective / cases
    difference = effectiveness - cocktail_effectiveness
    if difference > 0.05:
        print("better")
    elif difference < -0.05:
        print("worse")
    else:
        print("same")
