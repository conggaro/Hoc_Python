# Yêu cầu:
# 1. tạo số nguyên ngẫu nhiên "x" trong khoảng [1, 10]
# sử dụng randint(1, 10)

# 2. tính e^x
# 3. tính x giai thừa
# 4. tính logarit cơ số 10 của x
# 5. căn bậc 2 của x

import random
import math

# hàm tính e^x
def Ham_Tinh_e_Mu_x(thamSo):
    return math.pow(math.e, thamSo)

def Ham_TinhGiaiThua(thamSo):
    if thamSo == 0 or thamSo == 1:
        return 1
    
    else:
        return thamSo * Ham_TinhGiaiThua(thamSo - 1)

# hàm tính logarit cơ số 10 của x
def Ham_Tinh_Logarit_CoSo_10_Cua_x(thamSo):
    return math.log10(thamSo)

# hàm tính căn bậc 2 của x
def Ham_Tinh_CanBac_2_Cua_x(thamSo):
    return thamSo**(1/2)

# chương trình chính
x = random.randint(1, 10)

# gọi hàm tính e^x
ketQua1 = Ham_Tinh_e_Mu_x(x)
print(f"e^x = {ketQua1:{'.'}3f}")

# gọi hàm tính x giai thừa
ketQua2 = Ham_TinhGiaiThua(x)
print(f"{x}! = {ketQua2}")

# gọi hàm tính logarit cơ số 10 của x
ketQua3 = Ham_Tinh_Logarit_CoSo_10_Cua_x(x)
print(f"Logarit co so 10 cua {x} la: {ketQua3}")

# gọi hàm tính căn bậc 2 của x
ketQua4 = Ham_Tinh_CanBac_2_Cua_x(x)
print(f"Can bac 2 cua {x} la: {ketQua4}")