import random
import time

# Data nama mahasiswa dari foto
nama_laki_laki = [
    "241351082 MUKHAMAD RIZKI",
    "201351091 MUHAMMAD ZILDJIAN LAZUARDI",
    "221351009 ANANDA NUR HAFIZH",
    "241351004 ALIF PUTRA RAMADHAN",
    "241351039 FAJAR RUHYANA",
    "241351042 SATRIA WARINGIN JATI",
    "241351045 LATIF MIMBAR ROBANI",
    "241351066 GENTA ABDURRAHMAN",
    "241351076 ABDUL SOMAD MAULANA",
    "241351081 HERIER NUGRAHA",
    "241351098 DIMAS RIVALDI",
    "241351105 DANDI HASYARI PRIADI",
    "241351110 RAHMAT WILDAN",
    "241351112 FAHMI AKMAL MAULANA",
    "241351114 PURWA PUTRA PAMUNGKAS",
    "241351115 FAHRIZA AR RAHMAN",
    "241351131 DZAKY ZAIN AIDIL FITRAH",
    "241351138 RISDIKA WILIAM WANG",
    "241351141 YUGHA PUTRA IMANUDIN",
    "241351149 FIKRI AHMAD ZAELANI",
    "241351151 RIPQY PUTRA HIDAYAH"
]

# Data Perempuan
nama_perempuan = [
    "241352005 EVITA AULIA YASMIN",
    "241351041 ANDINI TRI AYUNI",
    "241351067 DEWINTA P M HUTASOIT",
    "241351085 FIRDA MEI NABILA",
    "241351088 FASYA SYALSABILA ROCHIM",
    "241351109 ROSSI ANDINI RAHAYU",
    "241351123 MELANI PUTRI KUSUMAH"
]

def distribusi_gender_balance(laki, perempuan, jumlah_kelompok, max_anggota=None):
    """
    Mendistribusikan mahasiswa dengan memastikan minimal 1 perempuan per kelompok
    dan membatasi jumlah maksimal anggota jika ditentukan
    """
    # Acak daftar
    laki_acak = laki.copy()
    perempuan_acak = perempuan.copy()
    random.shuffle(laki_acak)
    random.shuffle(perempuan_acak)
    
    kelompok = [[] for _ in range(jumlah_kelompok)]
    
    # Pastikan setiap kelompok dapat minimal 1 perempuan
    if len(perempuan_acak) < jumlah_kelompok:
        print(f"⚠️  Perhatian: Hanya ada {len(perempuan_acak)} perempuan untuk {jumlah_kelompok} kelompok.")
        print(f"    Tidak semua kelompok akan memiliki anggota perempuan.\n")
    
    # Distribusikan perempuan terlebih dahulu (1 per kelompok)
    for i in range(min(len(perempuan_acak), jumlah_kelompok)):
        kelompok[i].append(perempuan_acak[i])
    
    # Sisa perempuan didistribusikan merata dengan batasan max_anggota
    for i in range(jumlah_kelompok, len(perempuan_acak)):
        idx = i % jumlah_kelompok
        # Cari kelompok yang belum penuh
        if max_anggota:
            attempts = 0
            while len(kelompok[idx]) >= max_anggota and attempts < jumlah_kelompok:
                idx = (idx + 1) % jumlah_kelompok
                attempts += 1
        kelompok[idx].append(perempuan_acak[i])
    
    # Distribusikan laki-laki secara merata dengan batasan max_anggota
    for i, nama in enumerate(laki_acak):
        idx = i % jumlah_kelompok
        # Cari kelompok yang belum penuh
        if max_anggota:
            attempts = 0
            while len(kelompok[idx]) >= max_anggota and attempts < jumlah_kelompok:
                idx = (idx + 1) % jumlah_kelompok
                attempts += 1
        kelompok[idx].append(nama)
    
    # Acak urutan dalam setiap kelompok agar tidak terlihat pola
    for grup in kelompok:
        random.shuffle(grup)
    
    return kelompok

def buat_kelompok_by_anggota(max_anggota):
    """
    Membuat kelompok berdasarkan jumlah maksimal anggota per kelompok
    """
    total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)
    jumlah_kelompok = (total_mahasiswa + max_anggota - 1) // max_anggota
    
    return distribusi_gender_balance(nama_laki_laki, nama_perempuan, jumlah_kelompok, max_anggota)

def buat_kelompok_by_jumlah(jumlah_kelompok, max_anggota=None):
    """
    Membuat kelompok berdasarkan jumlah kelompok yang diinginkan
    dengan optional pembatasan maksimal anggota per kelompok
    """
    total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)
    
    # Jika max_anggota ditentukan, validasi dan sesuaikan jumlah kelompok jika perlu
    if max_anggota:
        min_kelompok_dibutuhkan = (total_mahasiswa + max_anggota - 1) // max_anggota
        if jumlah_kelompok < min_kelompok_dibutuhkan:
            print(f"\n⚠️  Dengan maksimal {max_anggota} anggota per kelompok,")
            print(f"    dibutuhkan minimal {min_kelompok_dibutuhkan} kelompok untuk {total_mahasiswa} mahasiswa.")
            print(f"    Jumlah kelompok akan disesuaikan dari {jumlah_kelompok} menjadi {min_kelompok_dibutuhkan}.\n")
            jumlah_kelompok = min_kelompok_dibutuhkan
    
    return distribusi_gender_balance(nama_laki_laki, nama_perempuan, jumlah_kelompok, max_anggota)

def hitung_gender(kelompok):
    """
    Menghitung jumlah laki-laki dan perempuan dalam kelompok
    """
    jumlah_perempuan = sum(1 for nama in kelompok if nama in nama_perempuan)
    jumlah_laki = len(kelompok) - jumlah_perempuan
    return jumlah_laki, jumlah_perempuan

def tampilkan_kelompok(kelompok):
    """
    Menampilkan hasil pembagian kelompok dengan efek delay
    """
    print("\n" + "="*60)
    print("HASIL PEMBAGIAN KELOMPOK")
    print("="*60)
    print("\n🎲 Mengacak kelompok...")
    time.sleep(1.5)
    
    for i, grup in enumerate(kelompok, 1):
        jumlah_laki, jumlah_perempuan = hitung_gender(grup)
        print(f"\n📌 KELOMPOK {i} ({len(grup)} anggota - 👨 {jumlah_laki} | 👩 {jumlah_perempuan}):")
        print("-" * 60)
        time.sleep(0.5)
        
        for j, nama in enumerate(grup, 1):
            gender_icon = "👩" if nama in nama_perempuan else "👨"
            print(f"   {j}. {gender_icon} {nama}")
            time.sleep(0.3)  # Delay untuk setiap anggota
        
        time.sleep(0.5)  # Delay setelah selesai satu kelompok
    
    print("\n" + "="*60)
    print("✅ Pembagian kelompok selesai!")
    print("="*60)

def main():
    total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)
    
    print("="*60)
    print("PROGRAM PENGACAKAN KELOMPOK MAHASISWA")
    print("="*60)
    print(f"Total mahasiswa: {total_mahasiswa}")
    print(f"  👨 Laki-laki: {len(nama_laki_laki)}")
    print(f"  👩 Perempuan: {len(nama_perempuan)}")
    print(f"\n⚖️  Setiap kelompok dijamin memiliki minimal 1 perempuan*")
    print(f"   (*jika jumlah kelompok ≤ {len(nama_perempuan)})")
    
    while True:
        print("\n📋 Pilih metode pembagian kelompok:")
        print("1. Berdasarkan jumlah maksimal anggota per kelompok")
        print("2. Berdasarkan jumlah kelompok yang diinginkan")
        print("3. Keluar")
        
        pilihan = input("\nPilihan Anda (1/2/3): ").strip()
        
        if pilihan == "1":
            try:
                max_anggota = int(input("\nMasukkan jumlah maksimal anggota per kelompok: "))
                if max_anggota < 2:
                    print("❌ Jumlah anggota harus minimal 2!")
                    continue
                if max_anggota > total_mahasiswa:
                    print(f"❌ Jumlah anggota tidak boleh lebih dari {total_mahasiswa}!")
                    continue
                
                kelompok = buat_kelompok_by_anggota(max_anggota)
                tampilkan_kelompok(kelompok)
                
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka.")
        
        elif pilihan == "2":
            try:
                jumlah_kelompok = int(input("\nMasukkan jumlah kelompok yang diinginkan: "))
                if jumlah_kelompok < 1:
                    print("❌ Jumlah kelompok harus minimal 1!")
                    continue
                if jumlah_kelompok > total_mahasiswa:
                    print(f"❌ Jumlah kelompok tidak boleh lebih dari {total_mahasiswa}!")
                    continue
                
                # Fitur baru: tanyakan apakah ingin membatasi max anggota
                batasi = input("\n🔢 Apakah ingin membatasi jumlah maksimal anggota per kelompok? (y/n): ").strip().lower()
                
                max_anggota = None
                if batasi == 'y':
                    try:
                        max_anggota = int(input("   Masukkan jumlah maksimal anggota per kelompok: "))
                        if max_anggota < 2:
                            print("❌ Jumlah anggota harus minimal 2!")
                            continue
                    except ValueError:
                        print("❌ Input tidak valid! Melanjutkan tanpa pembatasan.")
                        max_anggota = None
                
                kelompok = buat_kelompok_by_jumlah(jumlah_kelompok, max_anggota)
                tampilkan_kelompok(kelompok)
                
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka.")
        
        elif pilihan == "3":
            print("\n👋 Terima kasih telah menggunakan program ini!")
            break
        
        else:
            print("❌ Pilihan tidak valid! Pilih 1, 2, atau 3.")
        
        # Tanyakan apakah ingin mengacak lagi
        if pilihan in ["1", "2"]:
            lagi = input("\n🔄 Acak lagi? (y/n): ").strip().lower()
            if lagi != 'y':
                print("\n👋 Terima kasih telah menggunakan program ini!")
                break

if __name__ == "__main__":
    main()