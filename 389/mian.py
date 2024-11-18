def count_ways(n):
    # 初始化dp数组
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 1

    # 动态规划
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    # 返回总方案数
    return dp[n][0] + dp[n][1]

# 输入n
n = int(input())

# 输出方案数
print(count_ways(n))
