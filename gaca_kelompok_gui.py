import random
import tkinter as tk
from tkinter import ttk, messagebox

# Data nama mahasiswa dari foto
nama_afk = [
    # "241351018 KUSDINAR ASSIDIQ D",
    # "241351019 MOCHAMMAD DAFFA AL FARIZZI",
    # "241351028 MUHAMAD REKSA YOGA PRIATNA",
    # "241351047 DAFFA TAUFIQURRAHMAN SANTOSO",
    # "241351140 MUHAMMAD FADLAN KUSUMA",
    # "241351005 MUHAMMAD NUR MAULANA REVAN",
    # "241351143 ZIYAAD",
    # "221351108 NIDA DHIYA UL-HAQ",
    # "221351147 SYERLY NOVEBRIANA LAGONTANG",
]
nama_laki_laki = [
    "241351082 MUKHAMAD RIZKI"
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
    "241352005 EVITA AULIA YASMIN"
    "221351108 NIDA DHIYA UL-HAQ",
    "221351147 SYERLY NOVEBRIANA LAGONTANG",
    "241351041 ANDINI TRI AYUNI",
    "241351067 DEWINTA P M HUTASOIT",
    "241351085 FIRDA MEI NABILA",
    "241351088 FASYA SYALSABILA ROCHIM",
    "241351109 ROSSI ANDINI RAHAYU",
    "241351123 MELANI PUTRI KUSUMAH"
]

def distribusi_gender_balance(laki, perempuan, jumlah_kelompok, max_anggota=None):
    laki_acak = laki.copy()
    perempuan_acak = perempuan.copy()
    random.shuffle(laki_acak)
    random.shuffle(perempuan_acak)
    
    kelompok = [[] for _ in range(jumlah_kelompok)]
    
    # Distribusikan minimal 1 perempuan per kelompok (atau sebanyak perempuan yang tersedia)
    for i in range(min(len(perempuan_acak), jumlah_kelompok)):
        kelompok[i].append(perempuan_acak[i])

    # Sisa perempuan jika ada, distribusi ke kelompok lain, tetap perhatikan batas max_anggota
    for i in range(jumlah_kelompok, len(perempuan_acak)):
        idx = i % jumlah_kelompok
        if max_anggota:
            attempts = 0
            while len(kelompok[idx]) >= max_anggota and attempts < jumlah_kelompok:
                idx = (idx + 1) % jumlah_kelompok
                attempts += 1
            if attempts == jumlah_kelompok:
                break
        kelompok[idx].append(perempuan_acak[i])

    # Distribusi laki-laki ke kelompok, perhatikan max_anggota
    for i, nama in enumerate(laki_acak):
        idx = i % jumlah_kelompok
        if max_anggota:
            attempts = 0
            while len(kelompok[idx]) >= max_anggota and attempts < jumlah_kelompok:
                idx = (idx + 1) % jumlah_kelompok
                attempts += 1
            if attempts == jumlah_kelompok:
                break
        kelompok[idx].append(nama)

    # Acak urutan anggota dalam kelompok (agar tidak terlihat berpola)
    for grup in kelompok:
        random.shuffle(grup)
    
    return kelompok

def buat_kelompok_by_anggota(max_anggota):
    total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)
    jumlah_kelompok = (total_mahasiswa + max_anggota - 1) // max_anggota
    return distribusi_gender_balance(nama_laki_laki, nama_perempuan, jumlah_kelompok, max_anggota)

def buat_kelompok_by_jumlah(jumlah_kelompok, max_anggota=None):
    total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)
    if max_anggota:
        min_kelompok_dibutuhkan = (total_mahasiswa + max_anggota - 1) // max_anggota
        if jumlah_kelompok < min_kelompok_dibutuhkan:
            jumlah_kelompok = min_kelompok_dibutuhkan
    return distribusi_gender_balance(nama_laki_laki, nama_perempuan, jumlah_kelompok, max_anggota)

def hitung_gender(kelompok):
    jumlah_perempuan = sum(1 for nama in kelompok if nama in nama_perempuan)
    jumlah_laki = len(kelompok) - jumlah_perempuan
    return jumlah_laki, jumlah_perempuan

# ============ GUI BAGIAN ===========

class GroupAllocatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pengacakan Kelompok Mahasiswa")
        self.geometry("900x700")
        self.resizable(True, True)

        # DATA
        self.total_mahasiswa = len(nama_laki_laki) + len(nama_perempuan)

        # Widgets intialization
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="🎲 Pengacakan Kelompok Mahasiswa", font=("Arial", 20, "bold"))
        title.pack(pady=15)

        info = f"Total mahasiswa: {self.total_mahasiswa} (👨 {len(nama_laki_laki)}, 👩 {len(nama_perempuan)})"
        self.info_label = ttk.Label(self, text=info, font=("Arial", 12))
        self.info_label.pack()

        ttk.Label(self, text="Setiap kelompok dijamin minimal 1 perempuan\n(*jika jumlah kelompok ≤ jumlah perempuan)", foreground="#555", font=('Arial', 10)).pack(pady=(0,15))

        self.method_var = tk.IntVar(value=1)
        method_frame = ttk.Frame(self)
        method_frame.pack(pady=5)

        self.rb1 = ttk.Radiobutton(method_frame, text="1. Berdasarkan jumlah maksimal anggota per kelompok", variable=self.method_var, value=1, command=self.toggle_method)
        self.rb2 = ttk.Radiobutton(method_frame, text="2. Berdasarkan jumlah kelompok yang diinginkan", variable=self.method_var, value=2, command=self.toggle_method)
        self.rb1.grid(row=0, column=0, sticky='w', padx=5)
        self.rb2.grid(row=1, column=0, sticky='w', padx=5)

        # Entry max anggota
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=8)

        self.max_anggota_label = ttk.Label(self.input_frame, text="Jumlah maksimal anggota / kelompok:")
        self.max_anggota_entry = ttk.Entry(self.input_frame, width=10)
        self.max_anggota_label.grid(row=0, column=0, sticky="e", padx=2)
        self.max_anggota_entry.grid(row=0, column=1, padx=2)

        # Entry jumlah kelompok
        self.jumlah_kelompok_label = ttk.Label(self.input_frame, text="Jumlah kelompok yang diinginkan:")
        self.jumlah_kelompok_entry = ttk.Entry(self.input_frame, width=10)
        self.max_per_group_label = ttk.Label(self.input_frame, text=" Batasi max anggota / kelompok?")
        self.max_per_group_check = ttk.Checkbutton(self.input_frame, variable=tk.IntVar(), state="disabled") # for show only
        self.max_per_group_entry = ttk.Entry(self.input_frame, width=10)

        # Batasi max anggota pada mode 'jumlah kelompok'
        self.batasi_var = tk.BooleanVar(value=False)
        self.batasi_check = ttk.Checkbutton(self.input_frame, text="Batasi max anggota per kelompok", variable=self.batasi_var, command=self.toggle_batasi)
        self.max_anggota_label2 = ttk.Label(self.input_frame, text="Max anggota per kelompok:")
        self.max_anggota_entry2 = ttk.Entry(self.input_frame, width=10)

        # Info error
        self.error_var = tk.StringVar(value="")
        self.error_label = ttk.Label(self, textvariable=self.error_var, foreground="red")
        self.error_label.pack(pady=(4,0))

        # Tombol & hasil
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=7)
        self.shuffle_btn = ttk.Button(btn_frame, text="🎲 ACak Kelompok!", command=self.start_rolling_groups, style="Accent.TButton")
        self.shuffle_btn.pack(side="left", padx=(0,12))
        self.reset_btn = ttk.Button(btn_frame, text="🔄 Reset", command=self.reset_form)
        self.reset_btn.pack(side='left')

        self.progress_label = ttk.Label(self, text="", font=("Arial", 11, "italic"), foreground="#888")
        self.progress_label.pack(pady=(6,2))

        # Mulai modifikasi di sini: Tambahkan Canvas + Scrollbar
        frame_luar = ttk.Frame(self)
        frame_luar.pack(padx=5, pady=(5,20), fill='both', expand=True)

        self.canvas = tk.Canvas(frame_luar, borderwidth=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(frame_luar, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Agar isi frame bisa di-resize dan disesuaikan oleh canvas
        self.group_frame = ttk.Frame(self.canvas)
        self.group_frame_id = self.canvas.create_window((0,0), window=self.group_frame, anchor='nw')

        def _on_frame_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.group_frame.bind("<Configure>", _on_frame_configure)

        # scroll pakai mouse-wheel:
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.toggle_method()  # Untuk tampilkan field input default

    def toggle_method(self):
        # Bersihkan previous
        for w in self.input_frame.winfo_children():
            w.grid_forget()

        if self.method_var.get() == 1:
            self.max_anggota_label.grid(row=0, column=0, sticky="e", padx=2)
            self.max_anggota_entry.grid(row=0, column=1, padx=2)
        else:
            self.jumlah_kelompok_label.grid(row=0, column=0, sticky="e", padx=2)
            self.jumlah_kelompok_entry.grid(row=0, column=1, padx=2)
            self.batasi_check.grid(row=1, column=0, sticky='w', pady=(3,0), columnspan=2)
            if self.batasi_var.get():
                self.max_anggota_label2.grid(row=2, column=0, sticky='e', padx=2, pady=(1,0))
                self.max_anggota_entry2.grid(row=2, column=1, padx=2, pady=(1,0))

    def toggle_batasi(self):
        self.toggle_method()

    def reset_form(self):
        self.max_anggota_entry.delete(0, tk.END)
        self.jumlah_kelompok_entry.delete(0, tk.END)
        self.max_anggota_entry2.delete(0, tk.END)
        self.error_var.set("")
        self.progress_label.config(text="")
        for widget in self.group_frame.winfo_children():
            widget.destroy()
        # Reset scroll ke atas
        if hasattr(self, 'canvas'):
            self.canvas.yview_moveto(0)

    def start_rolling_groups(self):
        self.error_var.set("")
        for widget in self.group_frame.winfo_children():
            widget.destroy()
        self.progress_label.config(text="")

        # Scroll ke atas jika ada canvas
        if hasattr(self, 'canvas'):
            self.canvas.yview_moveto(0)

        method = self.method_var.get()
        kelompok = []
        if method == 1:
            try:
                maxa = int(self.max_anggota_entry.get())
                if maxa < 2: raise ValueError("Jumlah anggota harus minimal 2!")
                if maxa > self.total_mahasiswa: raise ValueError("Jumlah anggota tidak boleh lebih dari mahasiswa.")
                self.progress_label.config(text="🎲 Mengocok kelompok ...")
                self.after(800, lambda:self.show_with_animation(buat_kelompok_by_anggota(maxa)))
            except ValueError as e:
                self.error_var.set("❌ " + str(e))
                return
        else:
            try:
                jkel = int(self.jumlah_kelompok_entry.get())
                if jkel < 1: raise ValueError("Jumlah kelompok minimal 1")
                if jkel > self.total_mahasiswa: raise ValueError("Jumlah kelompok tidak boleh lebih dari mahasiswa.")
                max_anggota = None
                if self.batasi_var.get():
                    try:
                        max_anggota_is = int(self.max_anggota_entry2.get())
                        if max_anggota_is < 2:
                            raise ValueError("Jumlah anggota harus minimal 2!")
                        max_anggota = max_anggota_is
                    except ValueError:
                        self.error_var.set("❌ Input batas max anggota tidak valid.")
                        return
                self.progress_label.config(text="🎲 Mengocok kelompok ...")
                self.after(800, lambda:self.show_with_animation(buat_kelompok_by_jumlah(jkel, max_anggota)))
            except ValueError as e:
                self.error_var.set("❌ " + str(e))
                return

    # Bagian animasi peng-rol-an
    def show_with_animation(self, kelompok):
        self.progress_label.config(text="")
        for widget in self.group_frame.winfo_children():
            widget.destroy()
        N = len(kelompok)

        # Panel judul
        tk.Label(self.group_frame, text="Hasil Pembagian Kelompok", font=("Arial", 14, "bold")).pack(pady=2)

        self.rolling_state = {
            'kelompok': kelompok,
            'current_group': 0,
            'current_member': 0,
            'panels': []
        }
        # Buat panel-panel
        for i, anggota in enumerate(kelompok):
            # Frame per group
            gpanel = tk.LabelFrame(self.group_frame, text=f"Kelompok {i+1}", font=("Arial", 11, "bold"), padx=8, pady=2)
            gpanel.pack(pady=(10,0), fill='x')
            count_l, count_p = hitung_gender(anggota)
            info_str = f"👨 {count_l} | 👩 {count_p}   ({len(anggota)} anggota)"
            tk.Label(gpanel, text=info_str, font=("Arial", 10, "italic")).pack(anchor='w')
            list_panel = tk.Frame(gpanel)
            list_panel.pack(anchor='w')
            self.rolling_state['panels'].append({'frame': list_panel, 'anggota': anggota, 'labels':[]})

        # Pastikan canvas memperbarui ukuran dan scrollregion-nya
        self.group_frame.update_idletasks()
        if hasattr(self, 'canvas'):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self._rolling_add_member()

    def _rolling_add_member(self):
        state = self.rolling_state
        if state['current_group'] >= len(state['kelompok']):
            # Selesai
            self.progress_label.config(text="✅ Pembagian kelompok selesai!")
            # Paksa update scrollregion
            if hasattr(self, 'canvas'):
                self.group_frame.update_idletasks()
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            return

        idx_g = state['current_group']
        idx_m = state['current_member']
        anggota = state['panels'][idx_g]['anggota']
        panel = state['panels'][idx_g]['frame']

        if idx_m >= len(anggota):
            state['current_group'] += 1
            state['current_member'] = 0
            self.after(500, self._rolling_add_member)
            return

        nama = anggota[idx_m]
        gender_icon = "👩" if nama in nama_perempuan else "👨"
        rolling_label = tk.Label(panel, text=f"{idx_m+1}. {gender_icon} ", font=("Arial", 11))
        rolling_label.pack(anchor='w')

        # Animasi "rol" nama
        rolling_names = random.sample(nama_laki_laki + nama_perempuan, min(12, self.total_mahasiswa))
        if nama not in rolling_names:
            rolling_names[random.randint(0,len(rolling_names)-1)] = nama

        def animasi_rol(pos=0, rep=9):
            if rep == 0:
                rolling_label.config(text=f"{idx_m+1}. {gender_icon} {nama}")
                state['current_member'] += 1
                # Paksa update scrollregion setelah setiap nama baru
                if hasattr(self, 'canvas'):
                    self.group_frame.update_idletasks()
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"))
                self.after(400, self._rolling_add_member)
            else:
                show_nama = rolling_names[pos % len(rolling_names)]
                show_gender = "👩" if show_nama in nama_perempuan else "👨"
                rolling_label.config(text=f"{idx_m+1}. {show_gender} {show_nama}", foreground="#aaa" if rep > 2 else "#555")
                self.after(60+(10*(11-rep)), lambda: animasi_rol(pos+1, rep-1))

        animasi_rol()

# Jalankan
if __name__ == "__main__":
    app = GroupAllocatorApp()
    app.mainloop()