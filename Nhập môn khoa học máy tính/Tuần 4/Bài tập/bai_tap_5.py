# Yêu cầu:
# 1. nhập vào điểm toán
# 2. nhập vào điểm văn
# 3. nhập vào điểm tiếng Anh

# 4. in ra kết quả

# [8, 10]       --> Giỏi
# [6, 8)        --> Khá
# [4, 6)        --> Trung bình
# [0, 4)        --> Yếu
# Khác          --> Lỗi nhập điểm

diemToan = float(input(f"Nhap diem toan: "))

diemVan = float(input(f"Nhap diem van: "))

diemTiengAnh = float(input(f"Nhap diem tieng Anh: "))

diemTB = (diemToan + diemVan + diemTiengAnh) / 3

kiemTra1 = True if 0 <= diemToan and diemToan <= 10 else False

kiemTra2 = True if 0 <= diemVan and diemVan <= 10 else False

kiemTra3 = True if 0 <= diemTiengAnh and diemTiengAnh <= 10 else False

kiemTra = True if kiemTra1 == True and kiemTra2 == True and \
            kiemTra3 == True else False

if 8 <= diemTB and diemTB <= 10 and kiemTra:
    print(f"Ket qua: {diemTB:{'.'}3f}\nGioi")

elif 6 <= diemTB and diemTB < 8 and kiemTra:
    print(f"Ket qua: {diemTB:{'.'}3f}\nKha")

elif 4 <= diemTB and diemTB < 6 and kiemTra:
    print(f"Ket qua: {diemTB:{'.'}3f}\nTrung binh")

elif 0 <= diemTB and diemTB < 4 and kiemTra:
    print(f"Ket qua: {diemTB:{'.'}3f}\nYeu")

else:
    print(f"Loi nhap diem!")