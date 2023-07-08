# Mô tả:
# Họ tên của người Việt gồm 3 phần:
# 1. họ
# 2. tên đệm
# 3. tên

# Yêu cầu:
# 1. nhập họ tên đầy đủ
# 2. in ra họ
# 3. in ra tên
# 4. in ra tên đệm

ho_ten = input(f"Nhap ho va ten: ")

# hàm lấy họ
def Ham_LayHo():
    global ho_ten
    vi_tri = ho_ten.find(" ")
    ho = ho_ten[0: vi_tri: 1]
    return ho

# hàm lấy tên
def Ham_LayTen():
    global ho_ten
    vi_tri = ho_ten.rfind(" ")
    ten = ho_ten[vi_tri + 1: len(ho_ten): 1]
    return ten

# hàm lấy tên đệm
def Ham_LayTenDem():
    global ho_ten
    vi_tri1 = ho_ten.find(" ")
    vi_tri2 = ho_ten.rfind(" ")
    ten_dem = ho_ten[vi_tri1 + 1: vi_tri2: 1]
    return ten_dem

print("Ho:",Ham_LayHo())
print("Ten:",Ham_LayTen())
print("Ten dem:",Ham_LayTenDem())