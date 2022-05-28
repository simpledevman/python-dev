"""
program perulangan membaca buku dengan while
"""
book_count = 10
print("ibu perintah, baca semua bukumu")
read_count = 0

understood_count = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"buku ke {understood_count + 1} belum faham")
    else:
        understood_count = understood_count + 1
        print(f"buku ke {understood_count} sudah dibaca dan dipahami")


print(f"jumlah buku yang sudah dibaca dan dipahami {understood_count}")
if understood_count == book_count:
    print(f"bu, tidak semua buku bisa dipahami, "
          f" budi hanya bisa memahami {understood_count} buku")