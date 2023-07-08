# Yêu cầu:
# 1. nhập số nguyên dương n
# 2. in ra số hoàn chỉnh nhỏ hơn hoặc bằng n

# chương trình chính
n = int(input())

# hàm kiểm tra số hoàn chỉnh
def KiemTra_SHC(thamSo):
    tong = 0

    for i in range(1, thamSo, 1):
        if thamSo % i == 0:
            tong = tong + i
    
    if tong == thamSo:
        return True
    
    else:
        return False
    
# hàm in ra số hoàn chỉnh
# nhưng phải thỏa mãn 1 < n < 100000
def In_Ra_SHC():
    global n

    if 1 < n < 100000:
        for i in range(1, n + 1, 1):
            if KiemTra_SHC(i) == True:
                print(f"{i}", end=" ")

    else:
        print(f"N/A")

In_Ra_SHC()