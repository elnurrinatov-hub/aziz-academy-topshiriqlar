n = int(input())
eng_katta = -9999999999
orin = 1
for i in range(n):
    son = int(input())
    if son > eng_katta:
        eng_katta = son 
        orin = i + 1 
print(orin)