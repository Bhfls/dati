# BEGIN: 9ycx4j0n9bfi
n = int(input())
angles = list(map(int, input().split()))
sum_angles = sum(angles)
unknown_angle = (n - 2) * 180 - sum_angles
print(unknown_angle)
# END: 9ycx4j0n9bfi
