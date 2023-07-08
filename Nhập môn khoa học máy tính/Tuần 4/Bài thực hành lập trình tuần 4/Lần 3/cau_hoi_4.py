# Yêu cầu:
# 1. nhập vào số nguyên tương ứng với ngày
# 2. nhập vào số nguyên tương ứng với tháng
# 3. nhập vào số nguyên tương ứng với năm
# 4. in ra ngày/tháng/năm hôm qua
# 5. in ra ngày/tháng/năm ngày mai

ngay = int(input())

thang = int(input())

nam = int(input())

# tạo biến có kiểu danh sách
# biến này sẽ chứa tổng số ngày của 1 tháng

# tức là dùng cái biến "tháng" để làm chỉ số index
# để truy cập vào cái danh sách được luôn
# sau đó sẽ thu được tổng số ngày
danh_sach = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# nếu năm nhuận thì tháng 2
# có 29 ngày
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    danh_sach[1] = 29

# in ra hôm qua 
if ngay == 1:
    if thang == 1:
        print(f"31/12/{nam - 1}")
    
    elif thang != 1:
        # nếu tháng khác 1
        # thì in ra ngày cuối cùng của tháng trước
        print(f"{(danh_sach[thang - 2]):{'0'}>2}/{(thang - 1):{'0'}>2}/{nam}")
    
elif ngay != 1:
    print(f"{(ngay - 1):{'0'}>2}/{thang:{'0'}>2}/{nam}")

# in ra ngày mai
if ngay == danh_sach[thang - 1]:
    # đây là lập trình đối với những ngày cuối cùng của tháng
    if thang == 12:
        print(f"01/01/{nam + 1}")

    elif thang != 12:
        print(f"01/{(thang + 1):{'0'}>2}/{nam}")
    
elif ngay != danh_sach[thang - 1]:
    # đây là lập trình
    # xử lý những ngày không phải cuối tháng
    print(f"{(ngay + 1):{'0'}>2}/{thang:{'0'}>2}/{nam}")