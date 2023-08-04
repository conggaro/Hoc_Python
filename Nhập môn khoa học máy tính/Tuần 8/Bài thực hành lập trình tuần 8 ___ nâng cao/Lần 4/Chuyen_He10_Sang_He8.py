# Yêu cầu:
# 1. nhập chuỗi số n (hệ thập phân)
# 2. chuyển sang số hệ bát phân

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input("Nhap n: "))

# tạo biến số dư
so_du = 0

# tạo biến số bát phân
so_BatPhan = ""

while n != 0:
    so_du = n % 8
    n = n // 8
    so_BatPhan = so_BatPhan + str(so_du)

# hàm đảo ngược chuỗi
def Ham_DaoNguoc():
    global so_BatPhan
    return so_BatPhan[: : -1]

so_BatPhan = Ham_DaoNguoc()

print(so_BatPhan)