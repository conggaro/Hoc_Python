# Yêu cầu:
# 1. nhập vào 1 xâu gồm các chữ số
# 2. đếm và hiển thị số lần xuất hiện của số '0'

# 3. thống kê tất cả các chữ số
# và số lần xuất hiện của chữ số đó trong xâu

n = input(f"Nhap n: ")

dem_0 = 0

for item in n:
    if item == '0':
        dem_0 += 1

print(f"\nSo \'0\' xuat hien: {dem_0} lan")

dem_1 = dem_2 = dem_3 = dem_4 = \
            dem_5 = dem_6 = dem_7 = \
                dem_8 = dem_9 = 0

for item in n:
    if item == '1':
        dem_1 += 1

    elif item == '2':
        dem_2 += 1

    elif item == '3':
        dem_3 += 1

    elif item == '4':
        dem_4 += 1

    elif item == '5':
        dem_5 += 1

    elif item == '6':
        dem_6 += 1

    elif item == '7':
        dem_7 += 1

    elif item == '8':
        dem_8 += 1

    elif item == '9':
        dem_9 += 1

print(end="\n")

if dem_0 != 0:
    print(f"0: {dem_0}")

if dem_1 != 0:
    print(f"1: {dem_1}")

if dem_2 != 0:
    print(f"2: {dem_2}")

if dem_3 != 0:
    print(f"3: {dem_3}")

if dem_4 != 0:
    print(f"4: {dem_4}")

if dem_5 != 0:
    print(f"5: {dem_5}")

if dem_6 != 0:
    print(f"6: {dem_6}")

if dem_7 != 0:
    print(f"7: {dem_7}")

if dem_8 != 0:
    print(f"8: {dem_8}")

if dem_9 != 0:
    print(f"9: {dem_9}")