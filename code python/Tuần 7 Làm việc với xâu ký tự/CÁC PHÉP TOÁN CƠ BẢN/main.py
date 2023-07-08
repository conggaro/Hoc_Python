# toán tử cộng +
# có tác dụng nối xâu
str1 = "Hi"
str2 = "World"
print(str1 + " " + str2)

# toán tử nhân *
# có tác dụng nhân cái xâu str_xau lên n lần
str_xau = "A123"
print(str_xau * 3)

# toán tử hai chấm [ : : ]
# có tác dụng trả về 1 xâu con
# giống substr trong C++
# [bắt_đầu : kết_thúc : bước_nhảy]
# nó còn được gọi là phép cắt xâu

data = "Nguyen Van A"
ketQua = data[7 : 9 : 1]           # mong muốn lấy được xâu "Va"
print(f"{ketQua}")

# kiểm tra đúng sai
# bằng từ khóa "in"
laptop = "msi leopard"
ketQua_laptop = "eo" in laptop
print(ketQua_laptop)                # nếu có "eo" thì in ra True

# kiểm tra đúng sai
# bằng từ khóa "not in"
so = "12345"
ketQua_so = "5" not in so
print(ketQua_so)                    # nếu có "5" thì in ra False
