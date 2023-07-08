# s.split(phan_tach)
# có tác dụng tách chuỗi string
# và chuyển nó thành kiểu danh sách
str1 = "Nguyen Van An"

phan_tach = " "

print(str1.split(phan_tach))        # in ra ['Nguyen', 'Van', 'An']

# kiểu 2:
# s.split(phan_tach, [num])
# nó sẽ tạo ra (num + 1) phần tử

# nếu bạn viết s.split(phan_tach, 1)
# thì bạn sẽ được 2 phần tử

str2 = "Nguyen Van An"

phan_tach2 = " "

print(str2.split(phan_tach2, 1))        # in ra ['Nguyen', 'Van An']