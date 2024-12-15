n = int(input())
gold = 0
silver = 0
bronze = 0
for i in range(n):
    day = list(map(int, input().split()))
    gold += day[0]
    silver += day[1]
    bronze += day[2]
print(gold, silver, bronze, gold + silver + bronze)
