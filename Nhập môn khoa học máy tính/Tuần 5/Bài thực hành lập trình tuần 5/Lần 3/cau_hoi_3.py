# Yêu cầu:
# 1. nhập vào số nguyên n
# 2. in ra "Co" hoặc "Khong"

n = int(input())

# hàm kiểm tra số amstrong
def Ham_KiemTra_So_amstrong(thamSo):
    ketQua = False

    dem = 0

    clone1 = thamSo
    while clone1 != 0:
        dem = dem + 1
        clone1 = clone1 // 10

    clone2 = thamSo
    item = 0
    
    tong = 0

    while clone2 != 0:
        item = clone2 % 10
        tong = tong + item**dem
        clone2 = clone2 // 10

    if tong == thamSo:
        ketQua = True

    else:
        ketQua = False

    return ketQua

if Ham_KiemTra_So_amstrong(n):
    print(f"Co")

else:
    print(f"Khong")