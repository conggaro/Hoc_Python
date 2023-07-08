# Yêu cầu:
# 1. nhập số nguyên dương m
# 2. nhập số nguyên dương n
# 3. in ra số lượng các "số_nguyên_tố" nằm trong khoảng [m, n]

# viết hàm kiểm tra m, n có nằm trong khoảng (500, 100000) không
# nếu đúng          
# --> đếm số nguyên tố
# --> in ra màn hình

# nếu sai
# --> in ra "N/A"

# chương trình chính
m = int(input())
n = int(input())

# hàm kiểm tra số nguyên tố
# tức là bản thân cái số nguyên tố
# nó chỉ chia hết cho 1 và chính nó
def KiemTra_SoNguyenTo(thamSo):
    ketQua = False
    
    if thamSo < 2:
        ketQua = False

    elif thamSo >= 2:
        ketQua = True

        for i in range(2, int(thamSo**0.5) + 1, 1):
            if thamSo % i == 0:
                ketQua = False
                break
    
    return ketQua

# hàm in ra số lượng số nguyên tố
def Dem_SoLuong_SNT(thamSo1, thamSo2):
    kiemTra1 = True if 500 < thamSo1 < 100000 else False
    kiemTra2 = True if 500 < thamSo2 and thamSo2 < 100000 else False

    if kiemTra1 == True and kiemTra2 == True:
        dem = 0

        for i in range(thamSo1, thamSo2 + 1, 1):
            if KiemTra_SoNguyenTo(i) == True:
                dem += 1

        print(f"{dem}")

    else:
        print(f"N/A")

Dem_SoLuong_SNT(m, n)