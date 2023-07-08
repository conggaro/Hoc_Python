# Yêu cầu:
# 1. nhập vào số nguyên n
# 2. in ra "Co" hoặc "Khong"

n = int(input())

# hàm kiểm tra số nguyên tố
def KiemTra_SNT(thamSo):
    ketQua = False

    dem = 0

    for i in range(1, thamSo + 1, 1):
        if thamSo % i == 0:
            dem = dem + 1

    if dem == 2:
        ketQua = True

    else:
        ketQua = False

    return ketQua

if KiemTra_SNT(n):
    print(f"Co")

else:
    print(f"Khong")