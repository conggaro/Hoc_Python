# Yêu cầu:
# 1. nhập một chuỗi các số
# 2. thêm dấu phân tách hàng nghìn (dấu phẩy)

# |CHƯƠNG TRÌNH CHÍNH|
s = input()

# chuyển từ chuỗi string sang danh sách list
danh_sach = list(s)

# tạo biến index
index = len(s) - 1

# tạo biến đếm
dem = 0

# tạo biến khoi_tao
# để thêm các phần tử vào
khoi_tao1 = []

# tạo biến trạng thái
# nếu có dấu "." trong chuỗi
# thì trạng thái = 1
trang_thai = 0

if "." in s:
    trang_thai = 1

# tạo biến vị trí của dấu "."
vi_tri = -1

if trang_thai == 1:
    for i in range(0, len(s), 1):
        if s[i] == ".":
            vi_tri = i

for i in range (index, -1, -1):
    if trang_thai == 1:
        khoi_tao1.append(s[i])

        if i == vi_tri:
            trang_thai = 0

        continue

    dem +=1
    khoi_tao1.append(s[i])

    if s[i] == ".":
        dem = 0

    if dem == 3:
        khoi_tao1.append(",")
        dem = 0

if khoi_tao1[len(khoi_tao1) - 1] == ",":
    khoi_tao1.pop()

# đảo ngược lại biến khoi_tao1
khoi_tao2 = []

for i in range(len(khoi_tao1) - 1, -1, -1):
    khoi_tao2.append(khoi_tao1[i])

# chuyển từ danh sách về string
s = "".join(khoi_tao2)

print(s)