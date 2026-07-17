n = int(input())
musbat, manfiy = 0, 0
for _ in range(n):
    num = int(input())
    if num > 0:
        musbat += 1
    elif num < 0:
        manfiy += 1
print(musbat, manfiy)