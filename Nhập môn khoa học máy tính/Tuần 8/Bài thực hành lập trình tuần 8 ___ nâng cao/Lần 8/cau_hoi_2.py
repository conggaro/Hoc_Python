# Yêu cầu:
# 1. nhập mật khẩu
# 2. in ra "Strong Password" hoặc "Weak Password"

# |CHƯƠNG TRÌNH CHÍNH|
mat_khau = input()

# việc 1:
# kiểm tra độ dài >= 8
kiemTra1 = True if len(mat_khau) >= 8 else False

# việc 2:
# đếm chữ cái thường >= 2
dem_chu_thuong = 0
for item in mat_khau:
    if item.islower() == True:
        dem_chu_thuong += 1

kiemTra2 = True if dem_chu_thuong >= 2 else False

# việc 3:
# đếm chữ cái hoa >= 1
dem_chu_hoa = 0
for item in mat_khau:
    if item.isupper() == True:
        dem_chu_hoa += 1

kiemTra3 = True if dem_chu_hoa >= 1 else False

# việc 4:
# đếm chữ số >= 2
dem_chu_so = 0
for item in mat_khau:
    if item.isdecimal() == True:
        dem_chu_so += 1

kiemTra4 = True if dem_chu_so >= 2 else False

# việc 5:
# đếm ký tự đặc biệt >= 1
dem_KyTu = 0
for item in mat_khau:
    if item in "@#$%!":
        dem_KyTu += 1

kiemTra5 = True if dem_KyTu >= 1 else False

if kiemTra1 and kiemTra2 and kiemTra3 and \
        kiemTra4 and kiemTra5:
    print(f"Strong Password")

else:
    print(f"Weak Password")