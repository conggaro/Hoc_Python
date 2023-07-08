# Yêu cầu:
# 1. nhập số nhị phân x1
# 2. nhập số nhị phân x2
# 3. tính tổng x1, x2 ở dạng thập phân

# chương trình chính
x1 = x2 = ""

# hàm nhập dữ liệu
def NhapDuLieu():
    bien1 = input()
    bien2 = input()

    return bien1, bien2

# hàm kiểm tra số nhị phân
def KiemTra_SNP(thamSo):
    # tham số được truyền vào là dạng string

    ketQua = False

    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '1' or thamSo[i] == '0':
            ketQua = True

        else:
            ketQua = False
            break

    return ketQua

# hàm chuyển số nhị phân thành số thập phân
def Ham_Chuyen_SoNhiPhan_Sang_SoThapPhan(thamSo):
    # tham số truyền vào là dạng string

    so_mu = len(thamSo) - 1

    khoi_tao = 0

    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '1':
            khoi_tao = khoi_tao + 2**so_mu

        so_mu = so_mu - 1

    return khoi_tao

# hàm tính tổng
def Tinh_Tong():
    global x1, x2

    kiemTra1 = True if KiemTra_SNP(x1) == True else False
    kiemTra2 = True if KiemTra_SNP(x2) == True else False

    if kiemTra1 == True and kiemTra2 == True:
        bien1 = Ham_Chuyen_SoNhiPhan_Sang_SoThapPhan(x1)
        bien2 = Ham_Chuyen_SoNhiPhan_Sang_SoThapPhan(x2)

        print(f"{bien1 + bien2}")

    else:
        print(f"N/A")

x1, x2 = NhapDuLieu()

Tinh_Tong()