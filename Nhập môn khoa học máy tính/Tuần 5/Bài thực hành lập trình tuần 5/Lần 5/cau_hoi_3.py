# Yêu cầu:
# 1. nhập vào n
# 2. in ra bội của nó với các số từ 1,2,3,...,10

n = int(input())

for i in range(1, 10 + 1, 1):
    print(f"{n * i}")