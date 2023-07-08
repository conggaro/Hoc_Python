# Yêu cầu:
# 1. nhập điểm toán
# 2. nhập điểm văn
# 3. nhập điểm tiếng anh

# 4. in ra kết quả "Đỗ" hoặc "Trượt"
# tổng điểm > 25 thì đỗ

diem_toan = float(input(f"Nhap diem toan: "))

diem_van = float(input(f"Nhap diem van: "))

diem_tiengAnh = float(input(f"Nhap diem tieng Anh: "))

ketQua = (diem_toan + diem_van) * 2 + diem_tiengAnh

if 25 < ketQua:
    print(f"Ket qua: {ketQua}\nBan do.") # Kết quả: Bạn đỗ

elif 0 <= ketQua and ketQua <= 25:
    print(f"Ket qua: {ketQua}\nBan truot.")