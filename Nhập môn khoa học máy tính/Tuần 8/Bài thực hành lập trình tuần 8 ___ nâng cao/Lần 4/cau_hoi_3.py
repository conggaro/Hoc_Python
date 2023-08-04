# Yêu cầu:
# 1. nhập một chuỗi các số
# 2. thêm dấu phân tách hàng nghìn (dấu phẩy)

# |CHƯƠNG TRÌNH CHÍNH|
n = input()

# chuyển chuỗi số sang danh sách
danh_sach = list(n)

# tạo biến trạng thái
# trạng thái = 1
# tức là có dấu "." trong n
trang_thai = 0

if "." in n:
    trang_thai = 1

# nếu trạng thái = 1
# thì tìm vị trí của dấu "."
vi_tri = -1

vi_tri = n.rfind(".", 0, len(n))

# tạo biến đếm
dem = 0

# tạo biến khởi tạo
# để hứng dữ liệu
khoi_tao = []

for i in range(len(danh_sach) - 1, -1, -1):
    if trang_thai == 1:
        khoi_tao.append(danh_sach[i])

        if vi_tri == i:
            trang_thai = 0

        continue

    dem += 1
    khoi_tao.append(danh_sach[i])

    if dem == 3:
        khoi_tao.append(",")
        dem = 0

# nếu phần tử cuối cùng của khoi_tao
# là "," thì lấy nó ra
if khoi_tao[len(khoi_tao) - 1] == ",":
    khoi_tao.pop()

# chuyển danh sách sang chuỗi string
s = "".join(khoi_tao)

# hàm đảo ngược chuỗi string
def Ham_DaoNguoc(thamSo):
    return thamSo[: : -1]

print(Ham_DaoNguoc(s))