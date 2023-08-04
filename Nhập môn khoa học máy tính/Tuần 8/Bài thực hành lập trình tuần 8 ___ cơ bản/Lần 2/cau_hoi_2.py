# Yêu cầu:
# 1. nhập vào một chuỗi s
# 2. in ra "Yes" hoặc "No"

# biển số xe hợp lệ
# 11 ký tự
# 2 ký đầu là số
# 1 dấu gạch ngang
# 1 chữ cái
# 4 chữ số
# 1 dấu chấm
# 2 số
# 2 + 1 + 1 + 4 + 1 + 2 = 11 (ký tự)

# chương trình chính
s = input()

# lấy ra 2 ký tự đầu
lay_2_KyTu_Dau = s[0: 2: 1]

# việc 1:
# kiểm tra 2 ký đầu là số
kiemTra1 = lay_2_KyTu_Dau.isdecimal()

# việc 2:
# kiểm tra biển xe Hà Nội
# lấy 2 ký tự đầu đấy
# so sánh với 29, 30, 31
kiemTra2 = lay_2_KyTu_Dau in "29 30 31"

# việc 3:
# kiểm tra dấu gạch ngang
kiemTra3 = True if s[2] == "-" else False

# việc 4:
# kiểm tra chữ cái
kiemTra4 = True if s[3].isupper() == True else False

# việc 5:
# kiểm tra 4 chữ số
kiemTra5 = True if s[4: 8: 1].isdecimal() == True else False

# việc 6:
# kiểm tra 1 dấu chấm
kiemTra6 = True if s[8] == "." else False

# việc 7:
# kiểm tra 2 số
kiemTra7 = True if s[9: 11: 1].isdecimal() == True else False

if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4 and kiemTra5 and \
        kiemTra6 and kiemTra7:
    print(f"Yes")

else:
    print(f"No")