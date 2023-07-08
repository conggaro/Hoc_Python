# Yêu cầu:
# 1. nhập số nhị phân x1
# 2. nhập số nhị phân x2
# 3. kiểm tra 2 số đó có phải nhị phân hay không
# 4. nếu không phải thì in ra "N/A"
# 5. nếu phải thì in ra tổng 2 số đó ở dạng thập phân

# viết hàm chuyển đổi "số_nhị_phân" thành "số_thập_phân"
# viết hàm kiểm tra số nhị phân

# chương trình chính
x1 = input()
x2 = input()

# hàm kiểm tra số nhị phân
def KiemTra_SoNhiPhan(thamSo):
    ketQua = False

    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '0' or thamSo[i] == '1':
            ketQua = True
        
        else:
            ketQua = False

    return ketQua

# hàm chuyển đổi số nhị phân thành số thập phân
def Chuyen_SNP_Thanh_STP(thamSo):
    ketQua = 0

    so_mu = len(thamSo) - 1         # số mũ

    for i in range(0, len(thamSo), 1):
        if thamSo[i] == '1':
            ketQua = ketQua + 2**(so_mu)

        so_mu = so_mu - 1

    return ketQua

if KiemTra_SoNhiPhan(x1) == True and KiemTra_SoNhiPhan(x2) == True:
    data1 = Chuyen_SNP_Thanh_STP(x1)
    data2 = Chuyen_SNP_Thanh_STP(x2)
    
    print(f"{data1 + data2}")

else:
    print(f"N/A")