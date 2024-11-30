a, b = map(int, input().split())
print(a + b)
string = str(a + b)
if string == string[::-1]:
    print("Yes")
else:
    print("No")