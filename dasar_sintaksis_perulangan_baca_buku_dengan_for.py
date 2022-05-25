"""
program perulangan membaca buku
"""
jumlah_buku = 10
print("ibu perintah, baca semua buku")

jumlah_buku_yang_sudah_dibaca = 0

for jumlah_buku_yang_sudah_dibaca in range(1,jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")