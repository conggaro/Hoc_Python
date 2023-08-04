# Yêu cầu:
# 1. nhập một chuỗi các số (hệ thập phân)
# hệ thập phân còn gọi là hệ cơ số 10
# tức là nó dùng các số 0,1,2,3,4,5,6,7,8,9 để tạo ra các số đếm

# 2. in ra số đó (hệ nhị phân)
# 3. in ra số đó (hệ bát phân)
# 4. in ra số đó (hệ thập lục phân)

# |CHƯƠNG TRÌNH CHÍNH|
x = int(input())

# Hàm chuyển hệ thập phân sang nhị phân
def Chuyen_10_sang_2(thamSo):
    # tạo biến số dư (rem)
    so_du = 0

    # tạo biến số nhị phân
    so_NhiPhan = 0

    temp = 1

    while thamSo != 0:
        so_du = thamSo % 2
        thamSo = thamSo // 2
        so_NhiPhan = so_NhiPhan + so_du * temp
        temp = temp * 10

    return so_NhiPhan

# Hàm chuyển hệ thập phân sang bát phân
def Chuyen_10_sang_8(thamSo):
    # tạo biến số dư (rem)
    so_du = 0

    # tạo biến số bát phân
    so_BatPhan = 0

    temp = 1

    while thamSo != 0:
        so_du = thamSo % 8
        thamSo = thamSo // 8
        so_BatPhan = so_BatPhan + so_du * temp
        temp = temp * 10

    return so_BatPhan

# hàm đảo ngược chuỗi str
def Ham_DaoNguoc(thamSo):
    return thamSo[: : -1]

# Hàm chuyển hệ thập phân sang thập lục phân
def Chuyen_10_sang_16(thamSo):
    # tạo biến số dư (rem)
    so_du = 0

    # tạo biến danh sách
    danh_sach = []

    # tạo biến item
    item = ""

    while thamSo != 0:
        so_du = thamSo % 16
        thamSo = thamSo // 16

        if so_du <= 9:
            item = str(so_du)
        
        elif so_du == 10:
            item = "A"

        elif so_du == 11:
            item = "B"

        elif so_du == 12:
            item = "C"

        elif so_du == 13:
            item = "D"

        elif so_du == 14:
            item = "E"

        elif so_du == 15:
            item = "F"

        danh_sach.append(item)

        # chuyển danh sách sang chuỗi
        s = "".join(danh_sach)

    return Ham_DaoNguoc(s)

print(Chuyen_10_sang_2(x))
print(Chuyen_10_sang_8(x))
print(Chuyen_10_sang_16(x))