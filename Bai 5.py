m, n = map(int, input().split())
if (m / n != m // n):
    print(m // n + 1)
else:
    print(m // n)