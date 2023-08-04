# Yêu cầu:
# 1. nhập vào chuỗi s
# 2. in ra "Yes" hoặc "No"

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

# việc 1:
# kiểm tra chuỗi s
# là chính xác 11 ký tự
kiemTra1 = True if len(s) == 11 else False

# việc 2:
# kiểm tra 2 ký tự đầu là số
kiemTra2 = True if s[0: 2: 1].isdecimal() == True else False

# việc 3:
# kiểm tra dấu gạch ngang
kiemTra3 = True if s[2] == "-" else False

# việc 4:
# kiểm tra chữ cái
kiemTra4 = True if s[3].isupper() == True else False

# việc 5:
# kiểm tra 4 số
kiemTra5 = True if s[4: 8: 1].isdecimal() == True else False

# việc 6:
# kiểm tra dấu chấm
kiemTra6 = True if s[8] == "." else False

# việc 7:
# kiểm tra 2 số
kiemTra7 = True if s[9: 11: 1].isdecimal() == True else False

if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4 and \
        kiemTra5 and kiemTra6 and kiemTra7:
    print(f"Yes")

else:
    print(f"No")