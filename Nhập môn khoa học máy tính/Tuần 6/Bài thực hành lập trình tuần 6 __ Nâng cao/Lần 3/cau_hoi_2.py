# Yêu cầu:
# 1. nhập số nhị phân x1
# 2. nhập số nhị phân x2
# 3. tính tổng x1 + x2 ở dạng thập phân
# 4. in kết quả ra màn hình

# chương trình chính
x1 = input()
x2 = input()

# hàm kiểm tra số nhị phân
def KiemTra_SoNhiPhan(thamSo):
    ketQua = False

    # tham số ở dạng string
    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '0' or thamSo[i] == '1':
            ketQua = True
        
        else:
            ketQua = False
            break

    return ketQua

# hàm chuyển số nhị phân
# thành số thập phân
def Chuyen_NhiPhan_Sang_ThapPhan(thamSo):
    khoi_tao = 0

    so_mu = len(thamSo) - 1

    # tham số ở dạng string
    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '1':
            khoi_tao = khoi_tao + 2**so_mu
        
        so_mu = so_mu - 1

    return khoi_tao

# hàm tính tổng của 2 số nhị phân
# nhưng in kết quả ra số thập phân
def Tinh_Tong():
    global x1, x2

    kiemTra1 = True if KiemTra_SoNhiPhan(x1) else False
    kiemTra2 = True if KiemTra_SoNhiPhan(x2) else False

    if kiemTra1 == True and kiemTra2 == True:
        so_TP1 = Chuyen_NhiPhan_Sang_ThapPhan(x1)
        so_TP2 = Chuyen_NhiPhan_Sang_ThapPhan(x2)
        print(f"{so_TP1 + so_TP2}")

    else:
        print(f"N/A")

Tinh_Tong()