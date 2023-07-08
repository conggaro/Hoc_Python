# s.isupper()
# dùng để kiểm tra chữ hoa
# nếu có số thì vẫn được True

str1 = "ABCD"                   # True
str2 = "XYZ999"                 # True

str3 = "ABc"                    # False
str4 = "aaa"                    # False
str5 = "8888"                   # False

print(str1.isupper())
print(str2.isupper())

print(str3.isupper())
print(str4.isupper())
print(str5.isupper())