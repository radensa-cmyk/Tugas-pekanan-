# proyek_polling.py

# Struktur data survei
SURVEI = [
    {
        "pertanyaan": "Apa bahasa pemrograman favoritmu?",
        "opsi": ["Python", "JavaScript", "Java", "C++"]
    },
    {
        "pertanyaan": "Apa sistem operasi yang paling sering kamu gunakan?",
        "opsi": ["Windows", "macOS", "Linux"]
    },
    {
        "pertanyaan": "Tim mana yang akan menang di final piala dunia?",
        "opsi": ["Argentina", "Prancis", "Brasil", "Jerman"]
    }
]


hasil_polling = {}
for item in SURVEI:              # nginstal hasil polling dengan nilai 0
    for opsi in item["opsi"]:
        hasil_polling[opsi] = 0

print("="*44)
print("     SELAMAT DATANG DI APLIKASI POLLING")
print("="*44)


for idx, item in enumerate(SURVEI, start=1):      # tanyain user
    print(f"\nPertanyaan {idx}: {item['pertanyaan']}")
    for opsi in item["opsi"]:
        print(" -", opsi)

    
    while True:  #validasi
        jawaban = input("Jawaban Anda: ").strip()

        
        opsi_lower = [o.lower() for o in item["opsi"]]
        if jawaban.lower() in opsi_lower:
            # Cocokkan ke opsi asli agar kapitalisasi tetap benar
            for opsi in item["opsi"]:
                if jawaban.lower() == opsi.lower():
                    hasil_polling[opsi] += 1
                    print(">", opsi)
                    print("--- Terima kasih! ---")
                    break
            break
        else:
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")

# print
print("\n" + "="*44)
print("            HASIL POLLING")
print("="*44)

total_suara = sum(hasil_polling.values())
for opsi, jumlah in hasil_polling.items():
    persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
    print(f"{opsi} : {jumlah} suara ({persentase:.1f}%)")

print("="*44)

# Bonus sipen

with open("hasil_polling.txt", "w", encoding="utf-8") as f:
    for opsi, jumlah in hasil_polling.items():
        persentase = (jumlah / total_suara * 100) if total_suara > 0 else 0
        f.write(f"{opsi} : {jumlah} suara ({persentase:.1f}%)\n")
