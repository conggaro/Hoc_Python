# Yêu cầu:
# 1. nhập ngày
# 2. nhập tháng
# 3. nhập năm

# nhưng mà phải nhập cái chuỗi string cơ
# nó kiểu yyyy-MM-dd

# 4. in ra theo định dạng dd/MM/yyyy

thoi_gian = input(f"Nhap ngay thang nam: ")

# tạo biến phân tách
phan_tach = "-"

danh_sach = thoi_gian.split(phan_tach)

new_DanhSach = []
for i in range(len(danh_sach) - 1, 0 - 1, -1):
    new_DanhSach.append(danh_sach[i])

phan_tach2 = "/"

new_ThoiGian = phan_tach2.join(new_DanhSach)

print(f"Dinh dang moi: {new_ThoiGian}")