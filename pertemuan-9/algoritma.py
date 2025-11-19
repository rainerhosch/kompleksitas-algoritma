class Algoritma:
    """
    Sebuah kelas modular untuk mengukur performa 
    (waktu dan ruang) dari fungsi algoritma.
    """

    def __init__(self):
        """Inisialisasi pengukur."""
        # Kita bisa tambahkan pengaturan di sini nanti jika perlu
        pass
    def selection_sort(arr):
        """
        Implementasi Selection Sort dari Praktikum 1 [cite: 151-161].
        Kompleksitas Waktu: O(n^2)
        Kompleksitas Ruang Tambahan: O(1)
        """
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Operasi tukar (swap) terjadi in-place
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
    def bubble_sort(arr):
        """
        Implementasi Bubble Sort dari Praktikum 1 [cite: 163-173].
        Kompleksitas Waktu: O(n^2)
        Kompleksitas Ruang Tambahan: O(1)
        """
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def insertion_sort(arr):
        """
        Implementasi Insertion Sort dari Praktikum 1 [cite: 183-193].
        Kompleksitas Waktu: O(n^2) (Worst Case)
        Kompleksitas Ruang Tambahan: O(1)
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Pindahkan elemen
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # Tempatkan key di posisi yang benar
            arr[j + 1] = key

    def merge_sort(self, arr):
        """
        Implementasi Merge Sort dari Praktikum 2 [cite: 492-516].
        Kompleksitas Waktu: O(n log n)
        Kompleksitas Ruang Tambahan: O(n)
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            # Pembuatan list 'left' dan 'right' ini 
            # adalah sumber kompleksitas ruang O(n) 
            left = arr[:mid]
            right = arr[mid:]

            # Panggilan rekursif
            self.merge_sort(left)
            self.merge_sort(right)

            # Proses Merge
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1