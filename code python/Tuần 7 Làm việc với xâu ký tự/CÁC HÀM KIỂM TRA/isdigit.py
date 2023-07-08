# s.isdigit()
# chỉ là số thì in ra True
# nếu lẫn lộn cả chữ và số thì in ra False

str0 = "1.1"                        # False (ban đầu, tôi tưởng số 1.1 thì True)
str1 = "123"                        # True

str2 = "abc"                        # False
str3 = " 456"                       # False
str4 = "789 "                       # False
str5 = "abc999"                     # False

print(str0.isdigit())
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print(str4.isdigit())
print(str5.isdigit())