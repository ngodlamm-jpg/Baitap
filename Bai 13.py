n = int(input())
total = 0
if (n > 100):
    total += (n - 100) * 3000
    n = 100
if (n > 50):
    total += (n - 50) * 2000
    n = 50
if (n > 0):
    total += n * 1500
print(total)