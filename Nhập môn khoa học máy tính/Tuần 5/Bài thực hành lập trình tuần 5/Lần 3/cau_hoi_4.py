# Yêu cầu:
# 1. nhập a
# 2. nhập b
# 3. nhập c
# 4. nhập d

# 5. in ra bội chung nhỏ nhất

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# hàm tìm bội chung nhỏ nhất
def Ham_Tim_BCNN(bien1, bien2, bien3, bien4):
    ketQua = 0
    
    index_bat_dau = max(bien1, bien2, bien3, bien4)

    index_ket_thuc = bien1 * bien2 * bien3 * bien4

    for i in range(index_bat_dau, index_ket_thuc + 1, 1):
        kiemTra1 = True if i % bien1 == 0 else False
        kiemTra2 = True if i % bien2 == 0 else False
        kiemTra3 = True if i % bien3 == 0 else False
        kiemTra4 = True if i % bien4 == 0 else False

        if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4:
            ketQua = i
            break           # tức là tìm thấy số đầu tiên là phải break ngay

    return ketQua

print(f"{Ham_Tim_BCNN(a, b, c, d)}")