# Yêu cầu:
# 1. nhập n

# 2. in ra các số hoàn chỉnh
# nhỏ hơn hoặc bằng n

# chương trình chính
n = int(input())

# hàm kiểm tra số hoàn chỉnh
def KiemTra_SHC(thamSo):
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

# hàm in ra những số hoàn chỉnh
def In_Ra_SHC(thamSo):
    if 1 < thamSo < 100000:
        for i in range(1, thamSo + 1, 1):
            if KiemTra_SHC(i) == True:
                print(i, end=" ")
    
    else:
        print(f"N/A")

In_Ra_SHC(n)