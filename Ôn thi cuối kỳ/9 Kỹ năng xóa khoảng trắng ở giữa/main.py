# Ví dụ:
str1 = "Nguyen      Van     An"
print(f"Ban dau:\n\"{str1}\"")

# chuyển string sang danh sách
ds = str1.split(" ")

# tạo biến khởi tạo
khoi_tao = []

for i in range(0, len(ds), 1):
    if ds[i].isalpha() == True:
        khoi_tao.append(ds[i])

str1 = " ".join(khoi_tao)

print(f"\nLuc sau:\n\"{str1}\"")