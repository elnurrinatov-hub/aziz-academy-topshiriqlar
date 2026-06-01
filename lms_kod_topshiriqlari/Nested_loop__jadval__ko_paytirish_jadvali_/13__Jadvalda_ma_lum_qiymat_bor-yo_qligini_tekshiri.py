n, m = map(int, input().split())
x = int(input())
topiladi = False
for i in range(1, n + 1):
    if x % i == 0 and (x // i) <= m:
        topiladi = True
        break
if topiladi:
    print("Yes")
else:
    print("No")