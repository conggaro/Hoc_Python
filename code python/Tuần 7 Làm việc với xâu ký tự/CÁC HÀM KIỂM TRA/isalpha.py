# s.isalpha()
# chỉ có chữ cái thì in ra True
# nếu lẫn lộn cả chữ và số thì in ra False

str1 = "abc"                    # True
str2 = " abc"                   # False
str3 = "abc "                   # False
str4 = "xyz123"                 # False

print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print(str4.isalpha())