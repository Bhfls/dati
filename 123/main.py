c = input()
if 'A' <= c <= 'Z':
    print("upper")
elif 'a' <= c <= 'z':
    print("lower")
elif '0' <= c <= '9':
    print("digit")
else:
    print("other")
