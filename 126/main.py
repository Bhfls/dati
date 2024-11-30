a1,a2,a3,a4 = map(int,input().split())
if a1 > a2 and a2 > a3 and a3 > a4:
    print("Fish Diving")
elif a1 < a2 and a2 < a3 and a3 < a4:
    print("Fish Rising")
elif a1 == a2 and a2 == a3 and a3 == a4:
    print("Fish At Constant Depth")
else:
    print("No Fish")