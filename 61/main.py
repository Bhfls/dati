# BEGIN: 9ycx9j9949wx
def calculate_mortality_rate(confirmed_cases, deaths):
    mortality_rate = (deaths / confirmed_cases) * 100
    return mortality_rate

# 输入确诊数和死亡数
confirmed_cases, deaths = map(int, input().split())

# 计算死亡率
mortality_rate = calculate_mortality_rate(confirmed_cases, deaths)

# 输出死亡率，精确到小数点后3位
print(f"{mortality_rate:.3f}%")
# END: 9ycx9j9949wx
