# Yêu cầu:

# 1. nhập chiều dài m (mét)
# 2. nhập chiều rộng n (mét)

# 3. nhập vào a (đồng)
# tức là 1 mét vuông thì bán được a đồng tiền hoa

m = int(input("Nhap chieu dai m: "))
n = int(input("Nhap chieu rong n: "))
a = int(input("Nhap vao a dong: "))

dienTich = m * n

tong_tien = dienTich * a

print(f"So tien thu duoc la: {tong_tien} VND")

