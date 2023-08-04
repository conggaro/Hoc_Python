# Yêu cầu:
# 1. nhập vào 1 chuỗi ký tự
# 2. in ra "VALID"
# hoặc in ra "INVALID_" + vị trí

# |CHƯƠNG TRÌNH CHÍNH|
str1 = input()

# tìm vị trí của dấu chấm
vi_tri = str1.index(".")

# tạo biến trạng thái
# 0 là không có dấu "."
# 1 là có dấu "."
trang_thai = 0

# tạo biến kết quả
ketQua = ""

for i in range(0, len(str1), 1):
    if trang_thai == 0:
        if i == vi_tri:
            # đọc đến cái dấu chấm
            trang_thai = 1
            continue

        kiemTra1 = True if str1[i].isalpha() == True else False
        kiemTra2 = True if str1[i].isdigit() == True else False
        kiemTra3 = True if str1[i] == "_" else False

        if kiemTra1 or kiemTra2 or kiemTra3:
            ketQua = "VALID"
        
        else:
            ketQua = f"INVALID_{i + 1}"
            break
    
    elif trang_thai == 1:
        kiemTra1 = True if str1[i].isalpha() == True else False
        kiemTra2 = True if str1[i].isdigit() == True else False

        if kiemTra1 or kiemTra2:
            ketQua = "VALID"
        
        else:
            ketQua = f"INVALID_{i + 1}"
            break

print(ketQua)