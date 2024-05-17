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
    print(index)

print()

# in ra các số từ 5 đến 10
for index in range(5, 11):
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
        self.numericalOrder = Person.count

    # dấu "@" dùng để nói với trình biên dịch
    # đây là phương thức tĩnh
    @staticmethod
    def increment_count():
        Person.count += 1

    # phương thức bình thường
    def showInfo(self):
        return f"[{self.numericalOrder}, {self.fullName}, {self.age}, {self.gender}]"


# tạo đối tượng có kiểu dữ liệu Person
p = Person("Nguyễn Văn A", 20, True)

# in ra "số thứ tự"
print(p.numericalOrder)

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

# Nhập vào 1 số và kiểm tra số đó
<pre># hàm kiểm tra số nguyên
def IsInteger(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


# nhập vào vào số bất kỳ
x = input("Enter any number: ")


# nếu người dùng nhập sai
# thì người dùng phải nhập lại
while True:
    if IsInteger(x):
        print(f"It is {int(x)}.")
        break
    else:
        x = input("Please re-enter any number: ")</pre>

# Toán tử 3 ngôi
<pre>x = 10
status = "Lớn hơn 5" if x > 5 else "Không lớn hơn 5"
print(status)  # Kết quả: "Lớn hơn 5"</pre>

# Chuyển chuỗi string thành mảng
<pre>listItem_Str = "1,2,3,4,5,6"


# mảng ký tự
listItem = listItem_Str.split(",")
print(listItem)


# mảng số
listNumber = []
for i in range(len(listItem) - 1):
    item = int(listItem[i])
    listNumber.append(item)

print(listNumber)</pre>

# Chuyển mảng thành chuỗi string
<pre>list1 = [1, 2, 3, 4, 5, 6]
list2 = []

for item in list1:
    list2.append(str(item))

v_Str = ","

# phương thức join()
# chỉ hoạt động
# trong trường hợp tất cả phần tử
# của danh sách là kiểu dữ liệu string
listItem_Str = v_Str.join(list2)

print(listItem_Str)</pre>

# Tham trị trong python
<pre>"""
Tham trị (Pass by Value):
Khi truyền đối số vào hàm,
Python tạo một bản sao của giá trị đó
và gán cho tham số trong hàm.

Thay đổi giá trị của tham số trong hàm
không ảnh hưởng đến giá trị ban đầu
của biến bên ngoài hàm.
"""

def modify_value(x):
    x += 10
    print("Inside function:", x)

num = 5
modify_value(num)
print("Outside function:", num)</pre>

# Tham chiếu trong python
<pre>"""
Tham chiếu (Pass by Reference):
Khi truyền đối số vào hàm,
Python truyền địa chỉ của biến đó
(thay vì tạo bản sao giá trị).

Thay đổi giá trị của tham số trong hàm
ảnh hưởng trực tiếp đến giá trị
của biến bên ngoài hàm.

Tham chiếu thường áp dụng
cho các đối tượng có thể thay đổi
(như danh sách, từ điển, lớp, …).
"""

def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)</pre>

# Nhận biết kiểu dữ liệu của biến
<pre>a = 1
b = 9.9
c = "Hello"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))</pre>
