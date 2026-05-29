n = int(input())
n = list(map(int, input().split()))
mx = n[0]
for x in n:
    if x > mx:
        mx = x 
print(mx)