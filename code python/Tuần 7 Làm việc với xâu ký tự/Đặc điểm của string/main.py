# Xâu ký tự là bất biến

# không thể thêm hoặc bớt xâu ký tự

# không thể thay đổi ký tự của xâu

# khi thực hiện "+"
# thì 1 xâu mới sẽ được tạo ra để gán vào biến hiện tại

s = "hello PYTHON"

# s[0] = "N"                # viết kiểu này thì ngôn ngữ nào cũng báo lỗi

s_clone1 = s                
s_clone1 = "hi hi"          # viết như này thì OK

s_clone2 = s + " 1234"      # viết như này thì OK

print(f"Ban dau: {s}")
print(f"Luc sau 1: {s_clone1}")
print(f"Luc sau 2: {s_clone2}")