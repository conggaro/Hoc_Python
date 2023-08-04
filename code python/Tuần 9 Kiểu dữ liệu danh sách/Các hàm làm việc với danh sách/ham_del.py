# hàm del(danh_sach[index])
# có tác dụng
# xóa phần tử trong danh sách
# ở vị trí index

ds = [1, 2, 3, 4, 5, 6]

print(f"Danh sach ban dau:\n{ds}")

del(ds[0])

print(f"\nLuc sau:\n{ds}")

# kết quả:
# Danh sach ban dau:
# [1, 2, 3, 4, 5, 6]

# Luc sau:
# [2, 3, 4, 5, 6]