# Yêu cầu:
# 1. nhập số nguyên dương n

# 2. sử dụng kỹ thuật đệ quy để tính tổng
# các số nhỏ hơn hoặc bằng n

# chương trình chính
n = int(input())

# hàm tính tổng
# sử dụng đệ quy
def Tinh_Tong_DeQuy(thamSo):
    if thamSo == 1:
        return 1
    
    else:
        return thamSo + Tinh_Tong_DeQuy(thamSo - 1)
    
# hàm kiểm tra xem n
# có nằm trong khoảng (1, 10000) không
def KiemTra():
    global n

    if 1 < n < 10000:
        print(Tinh_Tong_DeQuy(n))

    else:
        print(f"N/A")

KiemTra()