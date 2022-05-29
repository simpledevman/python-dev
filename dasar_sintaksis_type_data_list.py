daftar_buku = ["seven habit","hary potter","succes story"]
# tampilkan variale dafta buku
print(daftar_buku)

# proses semua dengan ' for in'
print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

# tampilkan isi variable daftar_buku pada index tertentu
print("\ntampilkan isi daftar_buku pada index tertentu")
print(daftar_buku[0])
print(daftar_buku[1])
print(daftar_buku[2])

print("\ntampilkan  dengan for  in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1,"jurus menjadi bahagia", -4253,567]
print("\ntampilkan  dengan for  in range, dimana tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nkembalikan nilai awal daftar buku")
daftar_buku = ["seven habit","hary potter","succes story"]
print("\ntambakan 1 buku baru")
daftar_buku.append("resep sukses")
print(daftar_buku)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nclear list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nganti elemen pertama")
daftar_buku = ["seven habit","hary potter","succes story"]
daftar_buku[0] = "eight habits"
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nAmbil elemen ke 2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nbuku yang di ambil tadi")
print(buku)
daftar_buku.pop()

print("\npop")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\npop -1")
daftar_buku = ["seven habit","hary potter","succes story"]
daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nprintah del")
daftar_buku = ["seven habit","hary potter","succes story"]
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nperintah del dengan list comprehension")
daftar_buku = ["seven habit","hary potter","succes story"]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nperintah del dengan list comprehension start")
daftar_buku = ["seven habit","hary potter","succes story"]
del daftar_buku[0:1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nperintah del dengan list comprehension start")
daftar_buku = ["seven habit","hary potter","succes story"]
del daftar_buku[0:-2] # start : end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nperintah del dengan list comprehension start")
daftar_buku = ["seven habit","hary potter","succes story","bob sadino"]
del daftar_buku[0::2] # start : end : step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
