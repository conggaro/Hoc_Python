# xóa phần tử ở vị trí bất kỳ

def remove_char_at_position(string, position):
    # Chuyển đổi chuỗi thành danh sách
    danh_sach = list(string)

    # Xóa phần tử tại vị trí mong muốn
    del danh_sach[position]

    # Chuyển đổi lại danh sách thành chuỗi
    new_string = ''.join(danh_sach)

    return new_string

# Ví dụ sử dụng
str1 = "Hello, World!"
vi_tri = 5

# gọi hàm xóa phần tử ở vị trí bất kỳ
str_ketQua = remove_char_at_position(str1, vi_tri)

print(str_ketQua)