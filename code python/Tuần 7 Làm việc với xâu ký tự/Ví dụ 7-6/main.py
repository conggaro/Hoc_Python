# Yêu cầu:
# 1. nhập họ và tên
# 2. in ra họ
# 3. in ra tên
# 4. in ra tên đệm

ho_ten = input(f"Nhap ho va ten: ")

danh_sach = ho_ten.split(" ")

print(f"Ho: {danh_sach[0]}")
print(f"Ten: {danh_sach[len(danh_sach) - 1]}")

print(f"Ten dem: ", end="")
for i in range(1, len(danh_sach) - 1, 1):
    print(danh_sach[i], end=" ")

# sử dụng hàm join()
print()
print("-".join(danh_sach))