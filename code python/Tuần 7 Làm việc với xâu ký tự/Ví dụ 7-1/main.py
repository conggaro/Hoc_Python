# Yêu cầu:
# 1. kiểm tra trong tên có chữ "H" hoặc "h"

ho_ten = input("Nhap ho ten: ")

print(f"Ho ten cua ban la: {ho_ten}")

# tạo biến kiểm tra
kiemTra = False

for item in ho_ten:
    if item == 'H' or item == 'h':
        kiemTra = True
        break

if kiemTra == True:
    print(f"Trong ten cua ban co ky tu \"H\" hoac \"h\"")

else:
    print(f"Trong ten cua ban khong co ky tu \"H\" hoac \"h\"")