# mengambil input dari user

nama = input("masukan nama anda ")
print("selamat datang ", nama)
print("nilai dari nama", nama)
print(type(nama))

bil_int = int(input("masukan bilangan anda "))
print("bilangan anda adalah ", bil_int)
print("nilai dari bil_int", bil_int)
print(type(bil_int))

bil_float = float(input("masukan bilangan anda "))
print("bilangan anda adalah ", bil_float)
print("nilai dari bil_float", bil_float)
print(type(bil_float))

bil_bool = bool(input("masukan bilangan anda "))
print("bilangan anda adalah ", bil_bool)
print("nilai dari bil_bool", bil_bool)
print(type(bil_bool))


#buatlah program dengan output sebagai berikut
#  masukan nama anda :
#  masukkan umur anda :
#  nama anda adalah (nama)
#  tipe data dari nama anda adalah (tipe data dari nama)
#  umur anda adalah (umur)
#  tipe data dari umur anda adalah (tipe data umur)


nama = input("Masukkan nama anda : ")
umur = int(input("Masukkan umur anda : "))

print("Nama anda adalah", nama)
print("Tipe data dari nama anda adalah", type(nama))
print("Umur anda adalah", umur)
print("Tipe data dari umur anda adalah", type(umur))
