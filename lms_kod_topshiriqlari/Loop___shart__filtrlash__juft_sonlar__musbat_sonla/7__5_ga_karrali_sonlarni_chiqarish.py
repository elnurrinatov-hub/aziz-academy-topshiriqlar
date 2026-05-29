n = int(input())
sonlar = list(map(int, input().split()))
[print(x) for x in sonlar if x % 5 == 0]