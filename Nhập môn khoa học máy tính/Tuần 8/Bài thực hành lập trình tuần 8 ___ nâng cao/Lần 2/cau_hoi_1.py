# Yêu cầu:
# 1. nhập một chuỗi từ bàn phím
# 2. in ra "Strong Password" hoặc "Weak Password"

# |CHƯƠNG TRÌNH CHÍNH|
mat_khau = input()

# việc 1:
# kiểm tra chuỗi có độ dài >= 8
kiemTra1 = True if len(mat_khau) >= 8 else False

# việc 2:
# kiểm tra 2 chữ cái thường
dem_chu_thuong = 0
for i in range(0, len(mat_khau), 1):
    if mat_khau[i].islower() == True:
        dem_chu_thuong += 1
kiemTra2 = True if dem_chu_thuong >= 2 else False

# việc 3:
# kiểm tra 1 chữ cái hoa
dem_chu_hoa = 0
for i in range(0, len(mat_khau), 1):
    if mat_khau[i].isupper() == True:
        dem_chu_hoa += 1
kiemTra3 = True if dem_chu_hoa >= 1 else False

# việc 4:
# kiểm tra 2 chữ số
dem_chu_so = 0
for i in range(0, len(mat_khau), 1):
    if mat_khau[i].isdecimal() == True:
        dem_chu_so += 1
kiemTra4 = True if dem_chu_so >= 1 else False

# việc 5:
# kiểm tra 1 ký tự đặc biệt
dem_ky_tu = 0
for i in range(0, len(mat_khau), 1):
    if mat_khau[i] in "@#$%!":
        dem_ky_tu += 1
kiemTra5 = True if dem_ky_tu >= 1 else False

if kiemTra1 and kiemTra2 and kiemTra3 and \
        kiemTra4 and kiemTra5:
    print(f"Strong Password")

else:
    print(f"Weak Password")