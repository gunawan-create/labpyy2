# Mendefinisikan harga tiket
harga_reguler = 50000
harga_vip = 100000

# Meminta input dari pengguna
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

# Menentukan harga dasar tiket
if tipe_tiket == "reguler":
    total_harga = harga_reguler
elif tipe_tiket == "vip":
    total_harga = harga_vip
else:
    print("Tipe tiket yang Anda masukkan tidak valid.")
    total_harga = 0

# Menghitung diskon jika status member
diskon = 0.2 if status_member == "ya" else 0

# Menghitung total setelah diskon
total_harga = total_harga * (1 - diskon)

# Menampilkan total harga
if total_harga > 0:
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
