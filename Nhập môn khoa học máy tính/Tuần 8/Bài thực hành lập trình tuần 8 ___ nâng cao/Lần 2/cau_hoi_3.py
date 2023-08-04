# Yêu cầu:
# 1. nhập họ tên thứ nhất
# 2. nhập họ tên thứ hai
# 3. in ra "YES" hoặc "NO"

# tức là
# kiểm tra tất cả từ trong họ tên 2
# có nằm trong họ tên 1 không

# |CHƯƠNG TRÌNH CHÍNH|
ho_ten1 = input()
ho_ten2 = input()

danh_sach1 = ho_ten1.split(" ")
danh_sach2 = ho_ten2.split(" ")

kiemTra = False

for item in danh_sach2:
    if item in danh_sach1:
        kiemTra = True

    else:
        kiemTra = False
        break

if kiemTra == True:
    print(f"YES")

else:
    print(f"NO")