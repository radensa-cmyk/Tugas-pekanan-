def bersihkan_data():
    try:
        with open("transaksi_kotor.txt", "r") as file_input:
            with open("laporan_bersih.txt", "w") as file_output:
                file_output.write("LAPORAN TRANSAKSI BERSIH\n")
                file_output.write("=========================\n\n")

                grand_total = 0

                for baris in file_input:
                    if not baris.strip():
                        continue

                    baris = baris.strip()
                    data_potongan = baris.split(",")

                    id_transaksi = data_potongan[0].strip().upper()
                    nama_produk = data_potongan[1].strip().title()
                    jumlah = int(data_potongan[2].strip())
                    harga_satuan = float(data_potongan[3].strip())

                    total_harga = jumlah * harga_satuan
                    grand_total += total_harga

                    string_output = (
                        f"ID: {id_transaksi} | Produk: {nama_produk} | "
                        f"Jumlah: {jumlah} | Total Harga: Rp {total_harga}"
                    )

                    file_output.write(string_output + "\n")

                file_output.write("\n--- ANALISIS SELESAI ---\n")
                file_output.write(f"TOTAL KESELURUHAN: Rp {grand_total}\n")

        print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

    except FileNotFoundError:
        print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")


bersihkan_data()
