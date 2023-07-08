# Yêu cầu:
# 1. nhập một mật khẩu từ bàn phím
# 2. kiểm tra mật khẩu có mạnh không

# có tối thiểu 8 ký tự
# có ít nhất 1 chữ cái thường
# có ít nhất 1 chữ cái hoa
# có ít nhất 1 chữ số
# có ít nhất 1 ký tự đặc biệt @, #, $, %, !

mat_khau = input()

dem_ChuThuong = dem_ChuHoa = dem_So = dem_KyTu = 0

kiemTra = False

for item in mat_khau:
    if 'a' <= item and item <= 'z':
        dem_ChuThuong += 1

    elif 'A' <= item and item <= 'Z':
        dem_ChuHoa += 1

    elif '0' <= item and item <= '9':
        dem_So += 1

    elif item == '@' or item == '#' or item == '$' or item == '%' or item == '!':
        dem_KyTu += 1

if dem_ChuThuong > 0 and dem_ChuHoa > 0 and dem_So > 0 and dem_KyTu > 0:
    kiemTra = True

if len(mat_khau) >= 8 and kiemTra == True:
    print(f"Day la mat khau manh")

else:
    print(f"Day la mat khau yeu")