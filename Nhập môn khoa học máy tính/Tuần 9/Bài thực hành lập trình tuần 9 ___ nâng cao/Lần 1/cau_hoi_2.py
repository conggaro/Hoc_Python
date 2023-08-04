# Yêu cầu:
# 1. nhập chuỗi string

# 2. nếu đúng thì in ra "ARTIFICIAL"
# nếu sai thì in ra vị trí


# các nhà khoa học định nghĩa
# tính hiệu là "nhân tạo"
# nếu nó có dạng sóng chuẩn

# một tín hiệu số được gọi là sóng chuẩn
# nếu tất cả các giá trị của nó
# lớn hơn hoặc nhỏ hơn
# hai giá trị ngay trước và sau nó
# không tính giá trị đầu tiên
# không tính giá trị cuối cùng

# viết chương trình
# giúp nhà khoa học
# kiểm tra 1 tín hiệu
# thu được ngoài vũ trụ
# có phải "nhân tạo" không


# |CHƯƠNG TRÌNH CHÍNH|
chuoi_string = input()

# chuyển chuỗi string sang danh sách
ds = chuoi_string.split(" ")

ketQua = ""

for i in range(1, len(ds) - 1, 1):
    kiemTra1 = True if int(ds[i]) > int(ds[i - 1]) and int(ds[i]) > int(ds[i + 1]) else False
    kiemTra2 = True if int(ds[i]) < int(ds[i - 1]) and int(ds[i]) < int(ds[i + 1]) else False

    if kiemTra1 == True or kiemTra2 == True :
        ketQua = "ARTIFICIAL"

    else:
        ketQua = f"{i}"
        break

print(ketQua)