# Ví dụ:
str1 = "Nguyen Van Binh An"

ho = ""
ten_dem = ""
ten = ""

# tìm vị trí dấu cách đầu tiên
# từ trái sang phải
vi_tri1 = str1.find(" ")

# tìm vị trí dấu cách đầu tiên
# từ phải sang trái
vi_tri2 = str1.rfind(" ")

ho = str1[0: vi_tri1: 1]
ten_dem = str1[vi_tri1 + 1: vi_tri2: 1]
ten = str1[vi_tri2 + 1: : 1]

print(f"{'Ho:':<15}{ho}")
print(f"{'Ten dem:':<15}{ten_dem}")
print(f"{'Ten:':<15}{ten}")