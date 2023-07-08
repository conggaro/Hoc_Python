# Yêu cầu:
# sử dụng f-string với dữ liệu kiểu xâu

# kết quả in ra là: An********

name = "An"

print(f"{name:{'*'}^10}") # căn giữa biến name

print(f"{name:{'*'}<10}") # căn trái biến name

print(f"{name:{'*'}>10}") # căn phải biến name