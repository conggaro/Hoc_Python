# Yêu cầu
# 1. nhập một chuỗi số (Hệ thập phân)
# 2. chuyển sang hệ nhị phân

# |CHƯƠNG TRÌNH CHÍNH|
n = int(input("Nhap n: "))

# tạo biến số nhị phân
so_NhiPhan = ""

# tạo biến số dư
so_du = 0

while n != 0:
    so_du = n % 2
    n = n // 2
    so_NhiPhan = so_NhiPhan + str(so_du)

# hàm đảo ngược chuỗi string
def Ham_DaoNguoc():
    global so_NhiPhan
    return so_NhiPhan[: : -1]

# gọi hàm đảo ngược
so_NhiPhan = Ham_DaoNguoc()

print(so_NhiPhan)