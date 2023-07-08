# Yêu cầu:
# 1. số nguyên dương m
# 2. số nguyên dương n
# 3. đếm số nguyên tố trong khoảng [m, n]

# chương trình chính
m = int(input())
n = int(input())

# hàm kiểm tra số nguyên tố
def KiemTra_SNT(thamSo):
    if thamSo < 2:
        return False
    
    elif thamSo >= 2:
        for i in range(2, int(thamSo**0.5) + 1, 1):
            if thamSo % i == 0:
                return False
        
        return True
    
# hàm đếm số nguyên tố
# trong khoảng (500, 100000)
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

Dem_SNT()