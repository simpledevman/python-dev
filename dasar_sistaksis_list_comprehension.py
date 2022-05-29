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

print("\nmembuat list baru")
daftar_buku = ["seven habit","hary potter","succes story","bob sadino"]
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nmembuat list baru")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : ganjil")
daftar_buku = ["1 seven habit","2 hary potter","3 succes story","4 bob sadino"]
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : genap")
daftar_buku = ["1 seven habit","2 hary potter","3 succes story","4 bob sadino"]
daftar_buku_baru = daftar_buku[0::2] # start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : buang diujung")
daftar_buku = ["1 seven habit","2 hary potter","3 succes story","4 bob sadino"]
daftar_buku_baru = daftar_buku[0:-1:2] # buang di ujung lompat 2
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : ganjil")
daftar_buku = ["1 seven habit","2 hary potter","3 succes story","4 bob sadino"]
print(daftar_buku[0::2])