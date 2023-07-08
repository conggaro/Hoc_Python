# Yêu cầu:
# 1. nhập một chuỗi ký tự

# 2. kiểm tra xem có phải số điện thoại không
# "+84123456789"    --> hợp lệ

so_dien_thoai = input("Nhap so dien thoai: ")

# điều kiện
# 12 ký tự
# so_dien_thoai[0] == '+'
# so_dien_thoai[1, 2, 3,..., 11] là số isdecimal()

if len(so_dien_thoai) == 12:
    kiemTra1 = False
    kiemTra2 = False
    
    if so_dien_thoai[0] == '+':
        kiemTra1 = True

    for i in range(1, 11 + 1, 1):
        if so_dien_thoai[i].isdecimal() == True:
            kiemTra2 = True
        
        else:
            kiemTra2 = False
            break

    if kiemTra1 == True and kiemTra2 == True:
        print(f"Day la so dien thoai")

    else:
        print(f"Day khong phai so dien thoai")

else:
    print(f"Day khong phai so dien thoai")