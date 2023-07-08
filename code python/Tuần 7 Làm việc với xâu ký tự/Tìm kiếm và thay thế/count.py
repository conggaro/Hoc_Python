# s.count(substr)
# đếm số lần xuất hiện của xâu substr trong xâu s

str1 = "Nguyen Van Lan"

dem = str1.count("an")
print(dem)

# kiểu 2:
# s.count(substr, [start], [stop])
str2 = "Nguyen Van Lan"

dem2 = str2.count("an", 0, 10)
print(dem2)