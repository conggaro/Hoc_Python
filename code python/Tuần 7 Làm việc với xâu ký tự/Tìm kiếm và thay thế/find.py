# s.find(substr)
# trả về vị trí đầu tiên của xâu substr
# nếu không tìm thấy sẽ trả về -1

str1 = "Nguyen Van Lan"

vi_tri = str1.find("an")
print(vi_tri)

# kiểu 2:
# s.find(substr, [start], [stop])
str2 = "Nguyen Van Lan"

vi_tri2 = str2.find("an", 9)
print(vi_tri2)