def draw_pattern(rows, cols):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(rows):
        for j in range(cols):
            print(alphabet[(i + j) % len(alphabet)], end='')
        print()

# 绘制10×18的图形
draw_pattern(10, 18)
