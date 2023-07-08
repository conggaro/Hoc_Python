# Yêu cầu:
# 1. nhập a hàng
# 2. nhập b hàng
# 3. nhập c hàng
# 4. nhập d hàng

# 5. in ra số sinh viên tối thiểu

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# hàm tìm bội chung nhỏ nhất
def Ham_Tim_BCNN(thamSo1, thamSo2, thamSo3, thamSo4):
    index_bat_dau = max(thamSo1, thamSo2, thamSo3, thamSo4)

    index_ket_thuc = thamSo1 * thamSo2 * thamSo3 * thamSo4

    ketQua = 0

    for i in range(index_bat_dau, index_ket_thuc + 1, 1):
        kiemTra1 = True if i % thamSo1 == 0 else False
        kiemTra2 = True if i % thamSo2 == 0 else False
        kiemTra3 = True if i % thamSo3 == 0 else False
        kiemTra4 = True if i % thamSo4 == 0 else False

        if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4:
            ketQua = i
            break

    return ketQua

# gọi hàm tìm bội chung nhỏ nhất
x = Ham_Tim_BCNN(a, b, c, d)

print(f"{x}")