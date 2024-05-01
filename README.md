# Chạy chương trình Python bằng CMD
bước 1: điều hướng đến thư mục chứa file .py muốn chạy, có thể dùng câu lệnh "cd"<br>
bước 2: gõ <code>python tên_file.py</code>
<br>ví dụ: python showText.py

# Chuyển kiểu dữ liệu int sang string
<code>number = 42
string_number = str(number)
print(f"Chuỗi số nguyên: {string_number}")</code>

# Chuyển kiểu dữ liệu string sang int
<code>str_num = "123"
if str_num.isdigit():
    &nbsp;&nbsp;&nbsp;&nbsp;num = int(str_num)
    &nbsp;&nbsp;&nbsp;&nbsp;print(num)
else:
    &nbsp;&nbsp;&nbsp;&nbsp;print("Chuỗi không thể chuyển đổi thành số nguyên")</code>

# Chuyển kiểu dữ liệu string sang float
<code>
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


str_num = "3.14"
if isfloat(str_num):
    num = float(str_num)
    print(num)
else:
    print("Chuỗi không thể chuyển đổi thành số thập phân")</code>
