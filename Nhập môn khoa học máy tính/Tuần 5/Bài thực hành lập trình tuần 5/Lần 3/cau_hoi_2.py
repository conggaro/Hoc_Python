# Yêu cầu:
# 1. nhập số nguyên n
# 2. in ra bội của n với các số từ 1 đến 10

n = int(input())

for i in range(1, 10 + 1, 1):
    print(f"{(n * i)}")