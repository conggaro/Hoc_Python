# Yêu cầu:
# 1. nhập x1 (tọa độ góc trên bên trái)
# 2. nhập y1
# 3. nhập chiều dài (hình chữ nhật 1)
# 4. nhập chiều rộng (hình chữ nhật 1)

# 5. nhập x2 (tọa độ góc trên bên trái)
# 6. nhập y2
# 7. nhập chiều dài (hình chữ nhật 2)
# 8. nhập chiều rộng (hình chữ nhật 2)

# 9. in ra kết quả

# GIAO NHAU
# nếu 2 hình chữ nhật giao nhau

# KHÔNG GIAO NHAU
# nếu 2 hình không giao nhau

x1 = int(input())
y1 = int(input())
chieu_dai_1 = int(input())
chieu_rong_1 = int(input())

x2 = int(input())
y2 = int(input())
chieu_dai_2 = int(input())
chieu_rong_2 = int(input())

if (x1 + chieu_dai_1 < x2) or (x2 + chieu_dai_2 < x1):
    print(f"KHONGGIAONHAU")

elif (x1 + chieu_dai_1 >= x2) or (x2 + chieu_dai_2 >= x1):
    if (y1 + chieu_rong_1 < y2) or (y2 + chieu_rong_2 < y1):
        print(f"KHONGGIAONHAU")
    
    elif (y1 + chieu_rong_1 >= y2) or (y2 + chieu_rong_2 >= y1):
        print(f"GIAONHAU")