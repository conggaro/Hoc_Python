# Yêu cầu:
# 1. nhập chuỗi string

# 2. in ra kết quả
# "VALID"
# hoặc "INVALID_" + vị_trí

# |CHƯƠNG TRÌNH CHÍNH|
chuoi_string = input()

# tạo biến trạng thái
trang_thai = 0

# tạo biến vị trí dấu chấm
vi_tri = -1

# tìm vị trí dấu chấm
for i in range(0, len(chuoi_string), 1):
    if chuoi_string[i] == ".":
        vi_tri = i
        break

# tạo biến kết quả
ketQua = ""

for i in range(0, len(chuoi_string), 1):
    if trang_thai == 0:
        if i == vi_tri:
            trang_thai = 1
            continue

        kiemTra1 = True if chuoi_string[i].isalpha() == True else False
        kiemTra2 = True if chuoi_string[i].isdigit() == True else False
        kiemTra3 = True if chuoi_string[i] == "_" else False

        if kiemTra1 or kiemTra2 or kiemTra3:
            ketQua = "VALID"

        else:
            ketQua = f"INVALID_{i + 1}"
            break
    
    elif trang_thai == 1:
        kiemTra1 = True if chuoi_string[i].isalpha() == True else False
        kiemTra2 = True if chuoi_string[i].isdigit() == True else False

        if kiemTra1 or kiemTra2:
            ketQua = "VALID"

        else:
            ketQua = f"INVALID_{i + 1}"
            break

print(ketQua)