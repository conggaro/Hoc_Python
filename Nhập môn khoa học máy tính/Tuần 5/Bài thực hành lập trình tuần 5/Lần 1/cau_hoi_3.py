# Yêu cầu:
# 1. nhập n
# 2. in ra "Co" hoặc "Khong"

n = int(input())

# hàm kiểm tra số hoàn chỉnh
def KiemTra_SHC(thamSo):
    ketQua = False
    tong = 0

    for i in range(1, n, 1):
        if n % i == 0:
            tong = tong + i

    if tong == thamSo:
        ketQua = True
    
    else:
        ketQua = False

    return ketQua

if KiemTra_SHC(n) == True:
    print(f"Co")

else:
    print(f"Khong")