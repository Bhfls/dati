for i in range(1, 21):
    if i % 2 == 0 and i % 3 == 0:
        print("叮叮当当")
    elif i % 2 == 0:
        print("叮叮")
    elif i % 3 == 0:
        print("当当")
    else:
        print(i)
