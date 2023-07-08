# s.splitlines()
# nó có tác dụng trả về kiểu danh sách
# nó là các dòng trong xâu

# tức là nó thấy ký tự "\n"
# thì nó mới tách
str1 = "Nguyen Van An\nNguyen Van Binh"

danh_sach = str1.splitlines()

print(danh_sach)                # in ra ['Nguyen Van An', 'Nguyen Van Binh']

# kiểu 2:
# s.splitlines([num])
# chỉ cần thêm số 1
# là nó tự động cho cái "\n"
str2 = "Hi\nHello\nWelcome\nBye"

danh_sach2 = str2.splitlines(1)
print(danh_sach2)               # in ra ['Hi\n', 'Hello\n', 'Welcome\n', 'Bye']