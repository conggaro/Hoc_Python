# s.islower()
# dùng để kiểm tra chữ thường
# nếu có số thì vẫn được True

str1 = "abcd"                   # True
str2 = "xyz999"                 # True

str3 = "ABc"                    # False
str4 = "ABCDEF"                 # False
str5 = "8888"                   # False

print(str1.islower())
print(str2.islower())

print(str3.islower())
print(str4.islower())
print(str5.islower())