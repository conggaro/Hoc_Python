# Yêu cầu:
# 1. nhập vào số nguyên n
# 2. in ra "Co" hoặc "Khong"

n = int(input())

# hàm kiểm tra số hoàn chỉnh
def Ham_KiemTra_SoHoanChinh(thamSo):
    ketQua = False

    tong = 0

    for i in range(1, thamSo, 1):
        if thamSo % i == 0:
            tong = tong + i

    if tong == thamSo:
        ketQua = True

    else:
        ketQua = False

    return ketQua

if Ham_KiemTra_SoHoanChinh(n):
    print(f"Co")

else:
    print(f"Khong")