# Yêu cầu:
# 1. nhập chuỗi string
# 2. in ra "ARTIFICIAL" hoặc vị trí

# |CHƯƠNG TRÌNH CHÍNH|
chuoi_string = input()

# chuyển chuỗi string sang danh sách
ds = chuoi_string.split(" ")

ds2 = []

for i in range(0, len(ds), 1):
    ds2.append(int(ds[i]))

ketQua = ""

for i in range(1, len(ds2) - 1, 1):
    kiemTra1 = True if ds2[i] > ds2[i - 1] and ds2[i] > ds2[i + 1] else False
    kiemTra2 = True if ds2[i] < ds2[i - 1] and ds2[i] < ds2[i + 1] else False

    if kiemTra1 == True or kiemTra2 == True:
        ketQua = "ARTIFICIAL"

    else:
        ketQua = f"{i}"
        break

print(ketQua)