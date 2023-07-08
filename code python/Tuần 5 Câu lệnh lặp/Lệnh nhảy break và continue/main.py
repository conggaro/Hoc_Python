danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Ban dau:")
for i in danh_sach:
    print(f"{i}", end="  ")

print(f"\n\nVi du break:")
for i in danh_sach:
    if i == 5:
        break

    print(f"{i}", end="  ")

print(f"\n\nVi du continue:")
for i in danh_sach:
    if i == 5:
        continue

    print(f"{i}", end="  ")