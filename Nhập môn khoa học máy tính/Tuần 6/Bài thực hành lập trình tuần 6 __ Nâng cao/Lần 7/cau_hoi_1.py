# Yêu cầu:
# 1. nhập số nguyên dương m
# 2. nhập số nguyên dương n
# 3. đếm số nguyên tố trong khoảng [m, n]

from math import sqrt

# chương trình chính
m = n = 0

# hàm nhập dữ liệu
def NhapDuLieu():
    bien1 = int(input())
    bien2 = int(input())

    return bien1, bien2

# hàm kiểm tra số nguyên tố
def KiemTra_SNT(thamSo):
    if thamSo < 2:
        return False
    
    elif thamSo >= 2:
        for i in range (2, int(sqrt(thamSo)) + 1, 1):
            if thamSo % i == 0:
                return False
            
        return True
    
# hàm đếm số nguyên tố
# ràng buộc 500 < m, n < 100000
def Dem_SNT():
    global m, n

    kiemTra1 = True if 500 < m < 100000 else False
    kiemTra2 = True if 500 < n < 100000 else False

    if kiemTra1 == True and kiemTra2 == True:
        dem = 0

        for i in range(m, n + 1, 1):
            if KiemTra_SNT(i) == True:
                dem = dem + 1

        print(f"{dem}")

    else:
        print(f"N/A")

m,n = NhapDuLieu()

Dem_SNT()