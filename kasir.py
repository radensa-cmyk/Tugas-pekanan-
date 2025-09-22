def format_rupiah(angka):
    return "Rp {:,.2f}".format(angka).replace(",", ".").replace(".", ",", 1)

def tampilkan_header():
    print("============================================")
    print("      SELAMAT DATANG DI TOKO SERBAGUNA")
    print("============================================")

def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total

def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen = 10
    elif subtotal >= 200000:
        persen = 5
    else:
        persen = 0
    diskon = subtotal * persen / 100
    return diskon, persen

def tampilkan_struk(semua_nama, semua_harga, semua_jumlah, subtotal, total_diskon, persen_diskon):
    print("============================================")
    print("         STRUK PEMBELIAN ANDA")
    print("============================================")
    print("Detail Belanja:")
    for i in range(len(semua_nama)):
        total_item = semua_harga[i] * semua_jumlah[i]
        print(f"{i+1}. {semua_nama[i]} ({semua_jumlah[i]} x {format_rupiah(semua_harga[i])}) = {format_rupiah(total_item)}")
    print("--------------------------------------------")
    print(f"Subtotal            : {format_rupiah(subtotal)}")
    print(f"Diskon ({persen_diskon}%)        : - {format_rupiah(total_diskon)}")
    print("--------------------------------------------")
    print(f"Total yang harus dibayar: {format_rupiah(subtotal - total_diskon)}")
    print("============================================")
    print("      TERIMA KASIH TELAH BERBELANJA!")
    print("============================================")

daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

tampilkan_header()

while True:
    nama = input("Nama Barang: ")
    if nama.lower() == "selesai":
        break
    try:
        harga = float(input("Harga Satuan: Rp "))
        jumlah = int(input("Jumlah: "))
    except:
        print("Input tidak valid, coba lagi.")
        continue
    daftar_nama_barang.append(nama)
    daftar_harga_barang.append(harga)
    daftar_jumlah_barang.append(jumlah)
    print("--- Barang berhasil ditambahkan! ---")

subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
diskon, persen = hitung_diskon(subtotal)
tampilkan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal, diskon, persen)
