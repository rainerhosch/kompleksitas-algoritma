import time
import tracemalloc
import random

class Pengukur:
    """
    Sebuah kelas modular untuk mengukur performa 
    (waktu dan ruang) dari fungsi algoritma.
    """

    def __init__(self):
        """Inisialisasi pengukur."""
        # Kita bisa tambahkan pengaturan di sini nanti jika perlu
        pass

    def ukur_waktu(self, fungsi_algoritma, data, jumlah_eksekusi=1):
        """
        Mengukur waktu eksekusi murni (scratch code) menggunakan time.perf_counter.
        Menjalankan beberapa kali untuk rata-rata jika diminta.
        """
        total_waktu = 0
        
        for _ in range(jumlah_eksekusi):
            # Salin data agar setiap eksekusi adil (mendapat data acak)
            data_salinan = list(data)
            
            start_time = time.perf_counter()
            fungsi_algoritma(data_salinan)
            end_time = time.perf_counter()
            
            total_waktu += (end_time - start_time)
            
        return total_waktu / jumlah_eksekusi # Kembalikan rata-rata

    def ukur_ruang(self, fungsi_algoritma, data):
        """
        Mengukur penggunaan memori puncak (peak memory usage) 
        menggunakan library 'tracemalloc'.
        """
        # Salin data (kita hanya tertarik pada memori *algoritma*, 
        # bukan proses penyalinan data)
        data_salinan = list(data)
        
        tracemalloc.start()
        
        # Jalankan algoritma pada data salinan
        fungsi_algoritma(data_salinan)
        
        # Ambil statistik memori (saat ini, puncak)
        current, peak = tracemalloc.get_traced_memory()
        
        tracemalloc.stop()
        
        # Kembalikan penggunaan PUNCAK (peak)
        return peak

    def buat_data_acak(self, ukuran):
        """Helper untuk membuat list berisi angka acak."""
        return [random.randint(0, ukuran) for _ in range(ukuran)]