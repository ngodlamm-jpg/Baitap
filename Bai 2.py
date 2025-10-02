a, b = map(float, input().split())
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)