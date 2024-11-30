s, t = map(int, input().split())
if s <= 2:
    cost = 6 + t//3
elif 2 <= s:
    cost = 6 + t//3 + (s-2)*1.8
else:
    cost = 6 + 8*1.8 + (s-10)*2.7 + t//3

print(cost)