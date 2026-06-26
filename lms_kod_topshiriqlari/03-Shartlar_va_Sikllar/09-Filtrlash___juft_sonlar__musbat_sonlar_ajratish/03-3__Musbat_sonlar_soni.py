n = int(input())
arr = list(map(int, input().split()))
c = 0
for x in arr:
    if x > 0:
        c += 1
print(c)