# Yêu cầu:
# 1. nhập n
# 2. in ra bảng cửu chương bậc n

n = int(input("Nhap n: "))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in danh_sach:
    print(f"{n} * {i} = {n * i}")