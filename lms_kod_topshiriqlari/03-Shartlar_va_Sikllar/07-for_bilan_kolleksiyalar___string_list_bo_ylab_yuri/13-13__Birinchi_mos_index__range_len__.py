n = int(input())
a = []

while len(a) < n:
    a += list(map(int, input().split()))
x = int(input())

for i in range(n):
    if a[i] == x:
        print(i)
        break
        
else:
    print(-1)
