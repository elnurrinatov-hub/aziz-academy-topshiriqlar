a = int(input())
b = int(input())
yigindi = 0 
for num in range(a, b + 1):
    if num % 2 == 0:
        yigindi += num 
print(yigindi)