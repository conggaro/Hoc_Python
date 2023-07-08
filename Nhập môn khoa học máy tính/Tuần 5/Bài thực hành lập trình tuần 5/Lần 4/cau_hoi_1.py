# Yêu cầu:
# 1. nhập số nguyên n

# 2. in ra "Co" hoặc "Khong"
# nếu là số nguyên tố thì in ra có

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

n = int(input())

if KiemTra_SNT(n):
    print(f"Co")

else:
    print(f"Khong")