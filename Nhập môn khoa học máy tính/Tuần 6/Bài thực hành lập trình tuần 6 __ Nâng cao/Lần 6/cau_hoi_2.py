# Yêu cầu:
# 1. nhập số nguyên dương n
# 2. tính tổng trong khoảng [1, n]

# chương trình chính
n = int(input())

# hàm tính tổng
def Tinh_Tong(thamSo):
    if thamSo == 1:
        return 1
    
    else:
        return thamSo + Tinh_Tong(thamSo - 1)
    
# hàm in ra kết quả
# ràng buộc 1 < n < 10000
def In_Ra_KetQua():
    global n

    if 1 < n < 10000:
        tong = Tinh_Tong(n)

        print(f"{tong}")

    else:
        print(f"N/A")

In_Ra_KetQua()