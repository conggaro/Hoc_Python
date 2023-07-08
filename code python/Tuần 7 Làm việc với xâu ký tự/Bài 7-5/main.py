# Yêu cầu:
# 1. nhập vào một số

# 2. thêm dấu phẩy phân tách hàng nghìn
# nó kiểu ","

# ví dụ:
# nhập: 10000
# in ra: 10,000

from math import ceil

n = float(input(f"Nhap vao mot so: "))

# kiểm tra xem
# nó có phải cái loại số thập phân không
kiemTra = ceil(n)

if kiemTra > n:
    n = str(n)

elif kiemTra == n:
    n = int(n)
    n = str(n)

# việc 1:
# chuyển sang kiểu danh sách
danh_sach = list(n)

# tạo biến đếm
dem = 0

# tạo biến đánh dấu
# nếu tồn tại "." thì đánh dấu = 1
danh_dau = 0

# tạo biến vị trí
# để lưu vị trí có dấu "."
vi_tri = -1

# việc 2:
# kiểm tra xem tồn tại dấu "." không
for i in range(0, len(danh_sach), 1):
    if danh_sach[i] == ".":
        danh_dau = 1
        vi_tri = i

# cái new danh sách
# dùng để lưu số
# nhưng mà nó đảo ngược
new_DanhSach = []

for i in range(len(danh_sach) - 1, 0 - 1, - 1):
    if danh_dau == 1:
        if i >= vi_tri:
            new_DanhSach.append(danh_sach[i])

            if i == vi_tri:
                danh_dau = 0

            continue
    
    dem += 1

    new_DanhSach.append(danh_sach[i])

    if dem == 3:
        new_DanhSach.append(",")
        dem = 0

# đảo ngược lại để ra kết quả
ketQua = []

for i in range(len(new_DanhSach) - 1, 0 - 1, -1):
    ketQua.append(new_DanhSach[i])

    if ketQua[0] == ",":
        ketQua.pop()

# chuyển danh sách sang chuỗi string
new_n = "".join(ketQua)

print(new_n)