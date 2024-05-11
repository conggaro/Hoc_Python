try:
    listNumber = []

    # Đọc dữ liệu từ file .txt
    with open(r'C:\\Test code Python\\input.txt', 'r+') as file:
        print("Mở file thành công!")

        for line in file:
            print(line.strip())  # In từng dòng (loại bỏ ký tự xuống dòng)
            
            item = int(line.strip())
            listNumber.append(item)


    # In ra danh sách
    print(listNumber)


    # Xuống dòng
    print()


    # Hoặc bạn có thể đọc tất cả nội dung của file một lần:
    with open(r'C:\\Test code Python\\input.txt', 'r+') as file:
        print("Mở file thành công!")

        content = file.read()
        print(content)
except FileNotFoundError:
    print("Tệp không tồn tại hoặc không thể mở.")
except Exception as e:
    print(f"Lỗi: {e}")