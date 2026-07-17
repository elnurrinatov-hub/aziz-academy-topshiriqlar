n = int(input())
yigindi, soni = 0, 0
for _ in range(n):
    son = int(input())
    if son > 0:
        yigindi += son
        soni += 1
print(yigindi // soni if soni > 0 else 0)