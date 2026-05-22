n = int(input("Nhap so luong hoa don trong ca: "))
max_hd = 0
min_hd = 999999999
for i in range(1, n + 1):
    tien = int(input("Nhap gia tri hoa don thu " + str(i) + ": "))
    if tien > max_hd:
        max_hd = tien
    if tien < min_hd:
        min_hd = tien
print("---KET QUA KIEM TOAN CA RIKKEI STORE---")
print("Hoa don co gia tri cao nhat:", max_hd)
print("Hoa don co gia tri nho nhat:", min_hd)