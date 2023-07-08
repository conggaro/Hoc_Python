# Yêu cầu:
# 1. nhập a
# 2. nhập b
# 3. nhập c
# 4. nhập d
# 5. nhập e
# 6. in ra UCLN(a, b, c, d, e)

# hàm tìm ước chung lớn nhất
def Tim_UCLN(a, b, c, d, e):
    UCLN = 1

    # tạo index bắt đầu
    index_bat_dau = max(a, b, c, d, e)

    # tạo index kết thúc
    index_ket_thuc = 1

    for i in range(index_bat_dau, index_ket_thuc - 1, -1):
        kiemTra1 = True if a % i == 0 else False
        kiemTra2 = True if b % i == 0 else False
        kiemTra3 = True if c % i == 0 else False
        kiemTra4 = True if d % i == 0 else False
        kiemTra5 = True if e % i == 0 else False

        if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4 and kiemTra5:
            UCLN = i
            break

    return UCLN

# chương trình chính
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(f"{Tim_UCLN(a, b, c, d, e)}")