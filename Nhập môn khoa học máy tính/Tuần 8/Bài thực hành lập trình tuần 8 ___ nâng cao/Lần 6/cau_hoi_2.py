# Yêu cầu:
# 1. nhập họ tên thứ nhất
# 2. nhập họ tên thứ hai
# 3. in ra "YES" hoặc "NO"

# bản chất của bài toán này
# là lấy từng phần tử của "họ tên thứ hai"
# đem đi kiểm tra xem có tồn tại trong "họ tên thứ nhất" không

# |CHƯƠNG TRÌNH CHÍNH|
ho_ten1 = input()
ho_ten2 = input()

# chuyển chuỗi sang danh sách
danh_sach1 = list(ho_ten1)
danh_sach2 = list(ho_ten2)

# tạo biến kiểm tra
kiemTra = False

for item in danh_sach2:
    # kiểm tra xem cái item
    # có tồn tại trong danh sách 1 không
    if item in danh_sach1:
        kiemTra = True

    else:
        kiemTra = False
        break

if kiemTra == True:
    print(f"YES")

else:
    print(f"NO")