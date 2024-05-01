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
<pre>def isfloat(value):
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
    print("Chuỗi không thể chuyển đổi thành số thập phân")</pre>

# Vòng lặp for
<pre>for index in range(10):
    print(index)</pre>

# Lớp trong Python
<pre>class Person:
    # thuộc tính static
    count = 0

    # hàm khởi tạo constructor
    def __init__(self, parameter1, parameter2, parameter3):
        self.fullName = parameter1
        self.age = parameter2
        self.gender = parameter3
        Person.increment_count()

    # dấu "@" dùng để nói với trình biên dịch
    # đây là phương thức tĩnh
    @staticmethod
    def increment_count():
        Person.count += 1

    # phương thức bình thường
    def showInfo(self):
        return f"[{self.fullName}, {self.age}, {self.gender}]"


# tạo đối tượng có kiểu dữ liệu Person
p = Person("Nguyễn Văn A", 20, True)

# in ra "họ tên"
print(p.fullName)

# in ra tuổi
print(p.age)

# in ra giới tính
print(p.gender)

# gọi phương thức showInfo()
print(p.showInfo())

# truy cập thuộc tính tĩnh "count"
# ở bên trong lớp "Person"
print(Person.count)</pre>

# Mảng trong Python
<pre>arr_1 = [1, 2, 3, 4, 5]
arr_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(arr_1)
print(arr_2)</pre>

# Nhập/xuất trong Python
<pre>val = input("Enter your value: ")
print(val)</pre>
