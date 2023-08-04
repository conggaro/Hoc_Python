# Yêu cầu:
# 1. nhập chuỗi DNA thứ nhất
# 2. nhập chuỗi DNA thứ hai
# 3. in ra tỷ lệ hoặc "INVALID"

# từ "INVALID" nghĩa là không hợp lệ

# Chú ý: nhập 2 chuỗi DNA phải có độ dài bằng nhau

# kết quả chỉ lấy 2 chữ số sau dấu phẩy

# |CHƯƠNG TRÌNH CHÍNH|
DNA_1 = input()
DNA_2 = input()

if len(DNA_1) == len(DNA_2):
    # tạo biến đếm
    # sự giống nhau của 2 chuỗi DNA
    dem = 0

    for i in range(0, len(DNA_1), 1):
        if DNA_1[i] == DNA_2[i]:
            dem += 1

    # tạo biến tỷ lệ
    ty_le = dem / len(DNA_1)

    print(f"{ty_le:{'.'}2f}")

else:
    print(f"INVALID")