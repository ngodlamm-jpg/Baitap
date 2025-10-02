a = float(input())
b = float(input())
if (a == 0 and b != 0):
    print("vô nghiệm")
elif (a == 0 and b == 0):
    print("vô số nghiệm")
else:
    print(round(-b / a, 2))


