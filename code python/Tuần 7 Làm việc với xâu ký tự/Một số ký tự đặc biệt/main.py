# ví dụ "\n"
# dùng để xuống dòng
str1_1 = "Welcome to Python"
str1_2 = "Welcome\n to Python"

print(f"Ban dau: {str1_1}")
print(f"Luc sau: {str1_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ "\r"
# dùng để về đầu dòng (Enter), xong rồi nó bắt đầu ghi đè lên hết mấy cái đằng sau
str2_1 = "Nguyen Van A"
str2_2 = "Nguyen\r Van A"           # cái "\r" nó ghi đè luôn trên dòng đấy

print(f"Ban dau: {str2_1}")
print(f"Luc sau: {str2_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ "\t"
# dùng để Tab ra 1 khoảng
str3_1 = "Hello world"
str3_2 = "Hello\t\t world"

print(f"Ban dau: {str3_1}")
print(f"Luc sau: {str3_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ "\v"
# dùng để Tab dọc (tôi thấy nó giống ký tự "\n")
str4_1 = "abcd 1234"
str4_2 = "abcd\v 1234"

print(f"Ban dau: {str4_1}")
print(f"Luc sau: {str4_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ "\b"
# dùng để lùi trái (backspace)
str5_1 = "MNPQ"
str5_2 = "MNP\bQ"

print(f"Ban dau: {str5_1}")
print(f"Luc sau: {str5_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ "\f"
# là hết form (tôi thấy nó giống "\n")
str6_1 = "XYZ 369"
str6_2 = "XYZ\f 369"

print(f"Ban dau: {str6_1}")
print(f"Luc sau: {str6_2}")

print();                            # dùng để xuống dòng thôi

# ví dụ: \'
# có tác dụng in ra dấu nháy đơn
str7_1 = "Im a developer"
str7_2 = "I\'m a developer"

print(f"Ban dau: {str7_1}")
print(f"Luc sau: {str7_2}")

print();                            # dùng để xuống dòng thôi

# Ví dụ: \"
# có tác dụng in ra dấu nháy kép
str8_1 = "He said: Let go to the market"
str8_2 = "He said: \"Let go to the market\""

print(f"Ban dau: {str8_1}")
print(f"Luc sau: {str8_2}")

print();                            # dùng để xuống dòng thôi

# Ví dụ: \\
# có tác dụng in ra dấu sổ ngược
str9_1 = "C:Users nccon Videos code python main.py"
str9_2 = "C:\\Users\\nccon\\Videos\\code python\\main.py"

print(f"Ban dau: {str9_1}")
print(f"Luc sau: {str9_2}")