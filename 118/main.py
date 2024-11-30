# BEGIN: 9f4j4ld04wxr
num_pulls = 5  # 假设小华拉了5下开关

# 初始状态为灭
light_state = False

# 模拟拉动开关的操作
for _ in range(num_pulls):
    # 改变灯的状态
    light_state = not light_state

# 根据灯的状态输出结果
if light_state:
    print("灯亮")
else:
    print("灯灭")
# END: 9f4j4ld04wxr
