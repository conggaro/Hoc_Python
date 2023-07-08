# s.isalnum()
# là True
# nếu các ký tự trong xâu
# là chữ
# hoặc số
# NHƯNG PHẢI VIẾT LIỀN NHA

# nó giống kiểu tra
# nếu là số hoặc chữ thì in ra True
# thêm điều kiện phải viết liền nữa

str0 = "ok999"                  # True
str1 = "123"                    # True
str2 = "abc"                    # True

str3 = " 456"                   # False
str4 = "789 "                   # False
str5 = "abc 123"                # False

str6 = "567.89"                 # False

print(str0.isalnum())
print(str1.isalnum())
print(str2.isalnum())

print(str3.isalnum())
print(str4.isalnum())
print(str5.isalnum())
print(str6.isalnum())