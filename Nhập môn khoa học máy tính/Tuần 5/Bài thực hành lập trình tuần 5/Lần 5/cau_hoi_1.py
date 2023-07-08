# Yêu cầu:
# 1. nhập x     (ràng buộc x < y)
# 2. nhập y
# 3. tính tổng bình phương các số từ x đến y

x = int(input())

y = int(input())

tong = 0

for i in range(x, y + 1, 1):
    tong = tong + i**2

print(f"{tong}")