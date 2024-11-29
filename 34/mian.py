# 输入牛牛的作业成绩、小测成绩和期末考试成绩
# 输入牛牛的作业成绩、小测成绩和期末考试成绩
A, B, C = map(int, input().split())
# 计算总成绩
total_score = A * 0.2 + B * 0.3 + C * 0.5
# 输出总成绩
print(int(total_score))

