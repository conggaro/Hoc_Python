# Yêu cầu:
# 1. nhập n
# 2. viết hàm kiểm tra n có nằm trong khoảng [a, b] không
# 3. tính tổng các số nguyên dương nhỏ hơn hoặc bằng n
# 4. in ra "tổng" hoặc "N/A"

# hàm kiểm tra
# xem n có nằm trong khoảng [a, b] không
def KiemTra(n, a, b):
    if a <= n and n <= b:
        return True
    
    else:
        return False
    
# hàm tính tổng
def TinhTong(n):
    ketQua = 0

    if n == 1:
        ketQua = 1

    elif n != 1:
        ketQua = n + TinhTong(n - 1)

    return ketQua

# chương trình chính
n = int(input())

if KiemTra(n, 2, 999) == True:
    print(f"{TinhTong(n)}")

else:
    print(f"N/A")