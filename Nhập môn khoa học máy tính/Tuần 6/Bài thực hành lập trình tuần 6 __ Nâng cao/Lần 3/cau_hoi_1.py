# Yêu cầu:
# 1. nhập số nguyên dương n
# 2. nhập số nguyên dương m
# 3. đếm số đối xứng trong đoạn [n, m]

# chương trình chính
n = input()
m = input()

# hàm kiểm tra số đối xứng
def KiemTra_SoDoiXung(thamSo):
    thamSo = str(thamSo)

    khoi_tao = ""

    for i in range(len(thamSo) - 1, 0 - 1, -1):
        khoi_tao = khoi_tao + thamSo[i]

    if khoi_tao == thamSo:
        return True
    
    elif khoi_tao != thamSo:
        return False
    
# hàm đếm số đối xứng
# nhưng phải thỏa mãn trong khoảng (100 < n,m < 100000)
def Dem_SoDoiXung():
    global n, m
    
    kiemTra1 = True if 100 < int(n) < 100000 else False
    kiemTra2 = True if 100 < int(m) < 100000 else False
    
    dem = 0

    if kiemTra1 == True and kiemTra2 == True:
        for i in range(int(n), int(m) + 1, 1):
            if KiemTra_SoDoiXung(i) == True:
                dem = dem + 1

        print(f"{dem}")

    else:
        print(f"N/A")

Dem_SoDoiXung();