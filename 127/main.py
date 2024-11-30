hight, weight = map(float, input().split())
bmi = weight / (hight) ** 2

if bmi < 18.5:
    print("偏瘦")
elif 18.5 <= bmi < 25:
    print("正常")
elif 24<= bmi <=27.9:
    print("偏胖")
elif 28<= bmi <=39.9:
    print("肥胖")
else:
    print("极重度肥胖")