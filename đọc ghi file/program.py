"""
Quá trình đọc ghi file
bao gồm ba bước chính:
1. mở file
2. đọc hoặc ghi file
3. đóng file


Đầu tiên, chúng ta sẽ xem xét
các mode khi làm việc với file
trong Python nhé


Có một số mode thường được sử dụng
khi mở file trong Python:
1. Read Only (‘r’): Mode mặc định khi mở tệp.
Ở chế độ này, tệp chỉ được phép đọc dữ liệu
và con trỏ tệp bắt đầu ở vị trí đầu tệp.
Nếu tệp không tồn tại,
sẽ gặp ngoại lệ "FileNotFoundError".

2. Read & Write (‘r+’): Mở file cho phép cả đọc và ghi.
Vị trí con trỏ tệp ở vị trí đầu của tệp.
Nếu tệp không tồn tại,
sẽ gặp ngoại lệ "FileNotFoundError".

3. Write Only (‘w’): Mở file và chỉ cho phép ghi.
Vị trí con trỏ tệp ở vị trí đầu của tệp.
Nếu tệp không tồn tại, sẽ tự động tạo mới.
Nếu tệp đã tồn tại,
dữ liệu cũ sẽ bị ghi đè bằng dữ liệu mới.

4. Write & Read (‘w+’): Mở file cho phép cả đọc và ghi.
Vị trí con trỏ tệp ở vị trí đầu của tệp.
Nếu tệp không tồn tại, sẽ tự động tạo mới.
Nếu tệp đã tồn tại,
dữ liệu cũ sẽ bị ghi đè bằng dữ liệu mới.

5. Append Only (‘a’): Mở file cho phép ghi.
File sẽ được tạo mới nếu chưa tồn tại.
Con trỏ tệp sẽ ở cuối file
nên sẽ tiếp tục ghi dữ liệu
vào cuối
nếu ban đầu đã có dữ liệu.

Append & Read (‘a+’): Mở file cho phép ghi và đọc.
File sẽ được tạo mới nếu chưa tồn tại.
Con trỏ tệp sẽ ở cuối file
nên sẽ tiếp tục ghi dữ liệu
vào cuối
nếu ban đầu đã có dữ liệu.


Để mở file trong Python, chúng ta sử dụng hàm open()


Lưu ý: Ký tự r trước đường dẫn tới file
giúp bỏ qua các ký tự đặc biệt của string trong Python.
Ví dụ, nếu không có ký tự r,
thì \\t trong đường dẫn D:\\text\\myfile.txt
sẽ bị coi là dấu tab,
dẫn tới xảy ra lỗi không mong muốn


Để đóng file sau khi làm việc xong, sử dụng hàm close()
"""


try:
    # Mở tệp input.txt với mode 'w+'
    file_object = open(r'C:\\Test code Python\\input.txt', 'r+')
    
    print("Mở file thành công!")

    # Đặt con trỏ tệp về đầu tệp
    file_object.seek(0)

    # Đọc dữ liệu từ tệp
    data = file_object.read()

    # In ra dữ liệu đã đọc
    print(data)

    # Ghi dữ liệu vào tệp (ghi đè lên dữ liệu cũ luôn)
    # nếu muốn ghi tiếp thì bỏ cái dòng "file_object.seek(0)" đi
    # vì tôi đang cố tình đưa con trỏ chuột
    # về vị trí đầu để ghi đè
    file_object.seek(0)
    file_object.write("Hello, world!")
    
    # Đóng tệp
    file_object.close()
except FileNotFoundError:
    print("Tệp không tồn tại hoặc không thể mở.")
except Exception as e:
    print(f"Lỗi: {e}")