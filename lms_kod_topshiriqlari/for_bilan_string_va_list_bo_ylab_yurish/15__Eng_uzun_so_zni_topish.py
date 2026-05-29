q = input().split()

e = q[0]

for w in q:
    if len(w) > len(e):
        e = w
print(e)