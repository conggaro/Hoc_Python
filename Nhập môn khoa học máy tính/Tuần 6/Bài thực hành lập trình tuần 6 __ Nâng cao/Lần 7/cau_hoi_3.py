# Yêu cầu:
# 1. nhập số nguyên dương a
# 2. nhập số nguyên dương b
# 3. nhập số nguyên dương c
# 4. nhập số nguyên dương d
# 5. nhập số nguyên dương e
# 6. in ra UCLN(a, b, c, d, e)

# chương trình chính
a = b = c = d = e = 0

# hàm nhập dữ liệu
def NhapDuLieu():
    bien1 = int(input())
    bien2 = int(input())
    bien3 = int(input())
    bien4 = int(input())
    bien5 = int(input())

    return bien1, bien2, bien3, bien4, bien5

# hàm in ra UCLN(a, b, c, d, e)
def In_Ra_UCLN():
    global a, b, c, d, e

    # tạo index bắt đầu
    index_bat_dau = max(a, b, c, d, e)

    # tạo index kết thúc
    index_ket_thuc = 1

    UCLN = 0

    for i in range(index_bat_dau, index_ket_thuc - 1, -1):
        kiemTra1 = True if a % i == 0 else False
        kiemTra2 = True if b % i == 0 else False
        kiemTra3 = True if c % i == 0 else False
        kiemTra4 = True if d % i == 0 else False
        kiemTra5 = True if e % i == 0 else False

        if kiemTra1 and kiemTra2 and kiemTra3 and kiemTra4 and kiemTra5:
            UCLN = i
            break

    print(f"{UCLN}")

a, b, c, d, e = NhapDuLieu()

In_Ra_UCLN()