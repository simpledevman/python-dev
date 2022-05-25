"""
semua sintaksis dasar bahasa pemrograman terdiri dari:
1. sekuensial: langkah berurutan
2. percabangan: langkh melompat jika kondisi terpenuhi
3. perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# sekuensial
print("ibu berkata, 'pergi ke toko' ")
print("budi menjawab, 'baik , apa yang harus saya lakukan di toko?'")
print("ibu menjawab, 'beli satu botol susu, dan jika ada telur beli 6'")
print("maka budi berkangkat ke toko")
print("dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 173
jumlah_telur = 187
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("budi mengecek harganya, ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli susu")

print("budi pulang ke rumah")
print("menyerahkan hasilnya kepada ibu")