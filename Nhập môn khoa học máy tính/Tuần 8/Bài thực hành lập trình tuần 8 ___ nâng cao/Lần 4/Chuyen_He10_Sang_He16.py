# Yêu cầu:
# 1. nhập một chuỗi n (hệ thập phân)
# 2. chuyển sang hệ thập lục phân

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input("Nhap n: "))

# tạo biến số dư
so_du = 0

# tạo biến số thập lục phân
so_ThapLucPhan = ""

# tạo biến data
# để hứng dữ liệu mà tôi xử lý với số dư
data = ""

while n != 0:
    so_du = n % 16
    n = n // 16

    if so_du <= 9:
        data = str(so_du)
    elif so_du == 10:
        data = "A"
    elif so_du == 11:
        data = "B"
    elif so_du == 12:
        data = "C"
    elif so_du == 13:
        data = "D"
    elif so_du == 14:
        data = "E"
    elif so_du == 15:
        data = "F"

    so_ThapLucPhan = so_ThapLucPhan + data

# hàm đảo ngược chuỗi string
def Ham_DaoNguoc():
    global so_ThapLucPhan
    return so_ThapLucPhan[: : -1]

so_ThapLucPhan = Ham_DaoNguoc()

print(so_ThapLucPhan)