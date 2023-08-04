# Yêu cầu:
# 1. nhập một chuỗi số (hệ thập phân - cơ số 10)
# 2. in ra số hệ nhị phân (cơ số 2)
# 3. in ra số hệ bát phân (cơ số 8)
# 4. in ra số hệ thập lục phân (cơ số 16)

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input())

# hàm chuyển số hệ thập phân
# sang số hệ nhị phân
def Chuyen_He10_Sang_He2(thamSo):
    # tạo biến số dư
    so_du = 0

    # tạo biến số nhị phân
    so_NhiPhan = ""

    while thamSo != 0:
        so_du = thamSo % 2
        thamSo = thamSo // 2
        so_NhiPhan = so_NhiPhan + str(so_du)

    return so_NhiPhan

# hàm chuyển số hệ thập phân
# sang số hệ bát phân
def Chuyen_He10_Sang_He8(thamSo):
    # tạo biến số dư
    so_du = 0

    # tạo biến số bát phân
    so_BatPhan = ""

    while thamSo != 0:
        so_du = thamSo % 8
        thamSo = thamSo // 8
        so_BatPhan = so_BatPhan + str(so_du)

    return so_BatPhan

# hàm chuyển số hệ thập phân
# sang số hệ thập lục phân
def Chuyen_He10_Sang_He16(thamSo):
    # tạo biến số dư
    so_du = 0

    # tạo biến số thập lục phân
    so_ThapLucPhan = ""

    # tạo biến data
    # để xử lý số dư
    data = ""

    while thamSo != 0:
        so_du = thamSo % 16
        thamSo = thamSo // 16

        # xử lý số dư
        if so_du <= 9:
            data = str(so_du)

        elif so_du == 10:
            data = "A"

        elif so_du == 11:
            data = "B"

        elif so_du == 12:
            data = "C"

        elif so_du == 13:
            data = "D"

        elif so_du == 14:
            data = "E"

        elif so_du == 15:
            data = "F"

        so_ThapLucPhan = so_ThapLucPhan + data

    return so_ThapLucPhan

# hàm đảo ngược chuỗi string
def Ham_DaoNguoc(thamSo):
    return thamSo[: : -1]

print(Ham_DaoNguoc(Chuyen_He10_Sang_He2(n)))
print(Ham_DaoNguoc(Chuyen_He10_Sang_He8(n)))
print(Ham_DaoNguoc(Chuyen_He10_Sang_He16(n)))