# Yêu cầu:
# 1. nhập n
# 2. in ra "Co" hoặc "Khong"

# số hoàn chỉnh = tổng các ước nhỏ hơn nó

# ví dụ:
# 6 = 1 + 2 + 3

n = int(input())

tong = 0

for i in range(1, n, 1):
    if n % i == 0:
        tong = tong + i

if tong == n:
    print(f"Co")

else:
    print(f"Khong")