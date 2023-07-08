# Yêu cầu:
# 1. nhập số nguyên dương n
# 2. nhập số nguyên dương m
# 3. đếm số đối xứng trong đoạn [n, m]

# chương trình chính
n = m = 0

# hàm nhập dữ liệu
def NhapDuLieu():
    bien1 = input()
    bien2 = input()

    return bien1, bien2

# hàm kiểm tra số đối xứng
def KiemTra_SoDoiXung(thamSo):
    # tham số ở dạng string

    khoi_tao = ""

    for i in range(len(thamSo) - 1, 0 - 1, -1):
        khoi_tao = khoi_tao + thamSo[i]

    if khoi_tao == thamSo:
        return True
    
    else:
        return False

# hàm đếm số đối xứng
# ràng buộc 100 < n,m < 100000
def Dem_SoDoiXung():
    global n, m

    kiemTra1 = True if 100 < int(n) < 100000 else False
    kiemTra2 = True if 100 < int(m) < 100000 else False

    if kiemTra1 == True and kiemTra2 == True:
        dem = 0
        
        for i in range(int(n), int(m) + 1, 1):
            if KiemTra_SoDoiXung(str(i)) == True:
                dem = dem + 1

        print(f"{dem}")

    else:
        print(f"N/A")

n, m = NhapDuLieu()
Dem_SoDoiXung()