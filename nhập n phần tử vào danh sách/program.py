# nhập số
text = input("Nhập số lượng phần tử: ")
n = int(text)


# tạo danh sách
arr = []


# xuống dòng
print()


# nhập giá trị cho n phần tử
for index in range(0, n):
    message = "Nhập giá trị cho phần tử arr[" + str(index) + "] = "
    itemText = input(message)
    itemNumber = int(itemText)
    arr.append(itemNumber)


# in giá trị đã nhập ra màn hình
print("\nDanh sách phần tử vừa nhập:")

for index in range(0, len(arr)):
    print(arr[index], end = " ")


# tính tổng
total = 0

for item in arr:
    total = total + item

print("\n\nTổng = " + str(total))


# tính trung bình cộng
print("\nTrung bình cộng = " + str(total / n))


# xóa phần tử khỏi danh sách
indexText = input("\nNhập index cho phần tử muốn xóa: ")
indexNumber = int(indexText)
del(arr[indexNumber])

print("\nDanh sách sau khi xóa:")
print(arr)