# s.rfind(substr)
# trả về vị trí của xâu str
# nhưng nó tìm từ phải sang trái
str1 = "Nguyen Van Lan"

vi_tri = str1.rfind("an")
print(vi_tri)

# s.rfind(substr, [start], [stop])
str2 = "Nguyen Van Lan"

vi_tri2 = str2.rfind("an", 0, 10)
print(vi_tri2)