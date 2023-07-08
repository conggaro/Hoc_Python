# Yêu cầu:
# 1. nhập n
# 2. tính tổng các chữ số của n

n = int(input("Nhap n: "))

tong = 0

while n != 0:
    item = n % 10
    tong = tong + item

    n = n // 10

print(f"Tong = {tong}")