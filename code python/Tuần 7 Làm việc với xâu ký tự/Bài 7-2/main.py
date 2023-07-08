# Yêu cầu:
# 1. nhập tên của 3 thành phố trong nước
# 2. sắp xếp các thành phố theo thứ tự ABC

# 3. sắp xếp các thành phố theo thứ tự ABC
# không kể viết hoa hay thường

tp1 = input("Nhap Tp1: ")
tp2 = input("Nhap Tp2: ")
tp3 = input("Nhap Tp3: ")

# tạo danh sách
danh_sach = [tp1, tp2, tp3]

# hàm sắp xếp 1
def Ham_SapXep1():
    global danh_sach

    for i in range(0, len(danh_sach), 1):
        for j in range(i+1, len(danh_sach), 1):
            temp = ""
            
            if danh_sach[i] > danh_sach[j]:
                temp = danh_sach[i]
                danh_sach[i] = danh_sach[j]
                danh_sach[j] = temp

# hàm hiển thị 1
def HienThi_1():
    Ham_SapXep1()

    # in kết quả ra màn hình
    for item in danh_sach:
        print(f"{item}")

# hàm sắp xếp 2
def Ham_SapXep2():
    global danh_sach

    for i in range(0, len(danh_sach), 1):
        for j in range(i+1, len(danh_sach), 1):
            data1 = danh_sach[i].lower()
            data2 = danh_sach[j].lower()

            temp = ""
            
            if data1 > data2:
                temp = danh_sach[i]
                danh_sach[i] = danh_sach[j]
                danh_sach[j] = temp

# hàm hiển thị 2
def HienThi_2():
    Ham_SapXep2()

    # in kết quả ra màn hình
    for item in danh_sach:
        print(f"{item}")


# gọi hàm hiển thị 1
print()
HienThi_1()

# gọi hàm hiển thị 2
print()
HienThi_2()