while True:
    try:
        score = int(input("请输入成绩："))
        if 0 <= score <= 100:
            print(f"成绩：{score}")
            break
        else:
            print("输入有误，请重新输入。")
    except ValueError:
        print("输入有误，请重新输入。")
