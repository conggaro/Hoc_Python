# Ví dụ 1:
print("*" * 9)

print("*" + f"{'*':>8}")
print("*" + f"{'*':>8}")
print("*" + f"{'*':>8}")
print("*" + f"{'*':>8}")

print("*" * 9)


# ví dụ 2: căn lề trái
print()
print(f"{'*':<5}")
print(f"{'**':<5}")
print(f"{'***':<5}")
print(f"{'****':<5}")
print(f"{'*****':<5}")


# ví dụ 3: căn lề phải
print()
print(f"{'*':>5}")
print(f"{'**':>5}")
print(f"{'***':>5}")
print(f"{'****':>5}")
print(f"{'*****':>5}")


# ví dụ 4: căn lề giữa
print()
print(f"{'*':^5}")
print(f"{'***':^5}")
print(f"{'*****':^5}")
print(f"{'***':^5}")
print(f"{'*':^5}")