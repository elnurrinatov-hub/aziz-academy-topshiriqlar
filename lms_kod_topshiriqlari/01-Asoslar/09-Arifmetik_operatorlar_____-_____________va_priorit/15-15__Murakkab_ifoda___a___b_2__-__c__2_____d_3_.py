a, b, c, d = map(int, input().split())
res = (a + b*2) - (c//2) + (d%3)
print(f"Result: {res}")