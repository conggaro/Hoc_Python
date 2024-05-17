a = 0
for i in range(65, 65 + 26):
    a = a + 1
    
    if a % 10 == 0:
        print(chr(i))
    else:
        print(chr(i), end = " ")


# xuống dòng
print("\n")


b = 0
for i in range(97, 97 + 26):
    b = b + 1
    
    if b % 10 == 0:
        print(chr(i))
    else:
        print(chr(i), end = " ")