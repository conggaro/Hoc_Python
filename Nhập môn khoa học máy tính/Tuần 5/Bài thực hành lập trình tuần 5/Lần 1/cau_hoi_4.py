# Yêu cầu:
# 1. nhập n
# 2. in ra các bội của n với 1,2,3,...,10

n = int(input())

for i in range(1, 10 + 1, 1):
    print(f"{n * i}")