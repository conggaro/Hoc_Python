# Yêu cầu:
# 1. nhập số nguyên n
# 2. tính sc
# 3. tính sd

n = int(input())

sc = 0

sd = 0

for i in range(1, n + 1, 1):
    sc = (3 + sc)**(1/2)

print(f"{sc:{'.'}3f}")

tich = 1

for i in range(1, n + 1, 1):
    tich = tich * i
    sd = sd + tich

print(f"{sd:{'.'}3f}")