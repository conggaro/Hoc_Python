# Yêu cầu:
# 1. nhập n
# 2. nhập tỷ lệ thuế
# 3. nhập n phần tử
# 4. nhập giá tiền cho n phần tử
# 5. in ra tổng tiền

# lấy 1 chữ số sau dấu phẩy

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

ty_le_thue = float(input())

# danh sách số lượng
ds_SoLuong = []

# danh sách giá tiền
# tương ứng với số lượng
ds_GiaTien = []

for i in range(0, n, 1):
    item = float(input())
    ds_SoLuong.append(item)

for i in range(0, n, 1):
    item = float(input())
    ds_GiaTien.append(item)

tong_tien = 0

for i in range(0, n, 1):
    tong_tien = tong_tien + (ds_SoLuong[i] * ds_GiaTien[i])

tong_tien = tong_tien * (100 + ty_le_thue)/100

print(f"{tong_tien:{'.'}1f}")