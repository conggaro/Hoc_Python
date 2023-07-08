# s.replace(old, new)
# thay thế tất cả xâu old
# bằng xâu new
str1 = "Hi An An"

data = str1.replace("An", "Quan")
print(data, end="\n\n")

# kiểu:
# s.replace(old, new, [max])
# thay thế xâu old
# bằng xâu new
# với số lần max
str2 = "Hi An An"

data2 = str2.replace("An", "Quan", 1)
print(data2)