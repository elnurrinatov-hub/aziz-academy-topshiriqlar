n = int(input())
t = int(input())
s = 0 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j % t == 0:
            s += 1
print(s)