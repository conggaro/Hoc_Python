# Yêu cầu:
# 1. nhập chuỗi DNA thứ nhất
# 2. nhập chuỗi DNA thứ hai
# 3. in ra tỷ lệ giống nhau của 2 chuỗi DNA

# chú ý: phải nhập 2 chuỗi DNA có độ dài bằng nhau

# lấy 2 chữ số sau dấu chấm thập phân

# |CHƯƠNG TRÌNH CHÍNH|
DNA_1 = input()
DNA_2 = input()

if len(DNA_1) == len(DNA_2):
    # tạo biến đếm
    # để đếm phần tử giống nhau
    dem = 0
    
    # tạo biến index
    index = 0

    # tạo biến tổng
    # để lưu tổng số phần tử giống nhau
    # sau khi đếm xong
    tong = 0

    for item in DNA_1:
        dem = item.count(DNA_2[index])
        tong = tong + dem
        
        index += 1

    ty_le = tong / len(DNA_1)
    print(f"{ty_le:{'.'}2f}")

else:
    print("INVALID")