#Yêu cầu:
# 1. nhập n
# 2. kiểm tra n có phải số amstrong không

# số n có k chữ số
# tổng các lũy thừa bậc k của các chữ số

n = int(input())

# hàm kiểm tra số amstrong
def KiemTra_So_amstrong(thamSo):
    ketQua = False

    # tạo biến clone
    clone = thamSo

    dem = 0

    item = 0

    tong = 0

    # việc 1:
    # đếm số lượng chữ số
    while clone != 0:
        dem = dem + 1
        clone = clone // 10

    clone2 = thamSo

    # việc 2:
    # tính tổng
    while clone2 != 0:
        item = clone2 % 10
        tong = tong + item**dem
        clone2 = clone2 // 10

    if tong == thamSo:
        ketQua = True

    else:
        ketQua = False

    return ketQua

if KiemTra_So_amstrong(n):
    print(f"Co")

else:
    print(f"Khong")