# Yêu cầu:
# 1. nhập vào 1 chuỗi bất kỳ

# 2. chuyển chữ thường
# thành chữ hoa

# 3. chuyển chữ hoa
# thành chữ thường

# 4. viết hoa chữ cái đầu câu

# 5. viết hoa chữ cái ở đầu mỗi từ

# 6. viết thường các chữ cái ở đầu từ
# viết hoa các chữ cái không ở đầu từ

str1 = input("Nhap vao 1 chuoi: ")

print()
print(f"Ban dau: {str1}", end="\n\n")

print(f"Chuyen chu thuong thanh chu hoa:\n{str1.upper()}", end="\n\n")

print(f"Chuyen chu hoa thanh chu thuong:\n{str1.lower()}", end="\n\n")

print(f"Viet hoa chu cai dau cau:\n{str1.capitalize()}", end="\n\n")

print(f"Viet hoa chu cai o dau moi tu:\n{str1.title()}", end="\n\n")

def Ham_Abc_aBC(thamSo):
    thamSo = thamSo.title()
    thamSo = thamSo.swapcase()

    return thamSo

print(f"Viet thuong chu cai o dau moi tu\nva viet hoa cac chu dang sau: {Ham_Abc_aBC(str1)}", end="\n\n")