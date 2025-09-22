import os

def load_data(filename):
    data = {}
    if not os.path.exists(filename):
        return data
    with open(filename, 'r', encoding='utf-8') as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(',', 2)]
            if len(parts) < 2:
                print(f"Baris {lineno} diabaikan: format salah.")
                continue
            nis = parts[0]
            nama = parts[1]
            nilai_list = []
            if len(parts) == 3 and parts[2]:
                raw_vals = [v.strip() for v in parts[2].split(';') if v.strip() != '']
                for v in raw_vals:
                    try:
                        nilai_list.append(int(v))
                    except ValueError:
                        print(f"Nilai tidak valid di baris {lineno}: '{v}' diabaikan.")
            data[nis] = {'nama': nama, 'nilai': nilai_list}
    return data

def save_data(filename, data):
    lines = []
    for nis, info in data.items():
        nilai_str = ';'.join(str(x) for x in info.get('nilai', []))
        lines.append(f"{nis},{info.get('nama','')},{nilai_str}")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def get_grade(avg):
    if avg >= 85:
        return 'A'
    if avg >= 75:
        return 'B'
    if avg >= 65:
        return 'C'
    if avg >= 50:
        return 'D'
    return 'E'

def compute_stats(nilai_list):
    if not nilai_list:
        return 0, 0, 0, get_grade(0)
    avg = sum(nilai_list) / len(nilai_list)
    maksimum = max(nilai_list)
    minimum = min(nilai_list)
    grade = get_grade(avg)
    return avg, maksimum, minimum, grade

def lihat_daftar_siswa(data):
    if not data:
        print("Belum ada data siswa.")
        return
    print("--- Daftar Siswa ---")
    for nis in sorted(data.keys()):
        print(f"{nis}: {data[nis]['nama']}")

def lihat_detail_siswa(data):
    nis = input("Masukkan NIS: ").strip()
    if nis not in data:
        print("NIS tidak ditemukan.")
        return
    info = data[nis]
    avg, maksimum, minimum, grade = compute_stats(info.get('nilai', []))
    print(f"NIS: {nis}")
    print(f"Nama: {info.get('nama','')}")
    nilai_display = ', '.join(str(x) for x in info.get('nilai', [])) or "Tidak ada nilai"
    print(f"Nilai: {nilai_display}")
    print(f"Rata-rata: {avg:.2f}")
    print(f"Nilai Tertinggi: {maksimum}")
    print(f"Nilai Terendah: {minimum}")
    print(f"Grade Akhir: {grade}")

def tambah_siswa_baru(data):
    nis = input("Masukkan NIS baru: ").strip()
    if not nis:
        print("NIS tidak boleh kosong.")
        return
    if nis in data:
        print("NIS sudah ada. Tambah dibatalkan.")
        return
    nama = input("Masukkan Nama Lengkap: ").strip()
    data[nis] = {'nama': nama, 'nilai': []}
    print("Siswa berhasil ditambahkan.")

def tambah_nilai_siswa(data):
    nis = input("Masukkan NIS: ").strip()
    if nis not in data:
        print("NIS tidak ditemukan. Penambahan nilai dibatalkan.")
        return
    nilai_raw = input("Masukkan nilai baru (angka): ").strip()
    try:
        nilai = int(nilai_raw)
    except ValueError:
        print("Nilai harus berupa angka bulat. Dibatalkan.")
        return
    data[nis]['nilai'].append(nilai)
    print(f"Nilai {nilai} ditambahkan untuk NIS {nis}.")

def main():
    filename = "database_siswa.txt"
    data = load_data(filename)
    while True:
        print("\n--- Sistem Informasi Siswa ---")
        print("1. Lihat Daftar Siswa")
        print("2. Lihat Detail Siswa")
        print("3. Tambah Siswa Baru")
        print("4. Tambah Nilai Siswa")
        print("5. Simpan & Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == '1':
            lihat_daftar_siswa(data)
        elif pilihan == '2':
            lihat_detail_siswa(data)
        elif pilihan == '3':
            tambah_siswa_baru(data)
        elif pilihan == '4':
            tambah_nilai_siswa(data)
        elif pilihan == '5':
            save_data(filename, data)
            print("Data berhasil disimpan. Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
