#  Prediksi Hujan Australia

Repository ini berisi seluruh alur pembersihan data, analisis eksploratif (EDA), hingga penyiapan data untuk memprediksi apakah besok akan turun hujan berdasarkan data cuaca harian di Australia.

##  Ringkasan Proyek

Tujuan utama dari alur kerja ini adalah menyiapkan data yang bersih dan siap pakai untuk pemodelan *machine learning*.

* **Ukuran Data Akhir:** 41.564 baris × 23 kolom
* **Variabel Target:** `RainTomorrow` (Klasifikasi: Ya / Tidak)

##  Tahapan Preprocessing & Analisis

1. **Pembersihan Outlier (Pencilan)**
   * Menangani nilai-nilai ekstrem pada fitur numerik menggunakan metode *Interquartile Range* (IQR).

2. **Standardisasi Data**
   * Mengubah skala fitur numerik dengan `StandardScaler` agar distribusi data terpusat di angka 0.

3. **Cek Duplikat & Missing Values**
   * Memastikan data bebas dari baris ganda dan tidak ada lagi nilai kosong di seluruh kolom.

4. **Encoding Fitur Kategorikal**
   * Mengubah variabel teks (seperti `Location`, arah angin, dan status hujan) menjadi format angka bulat menggunakan `LabelEncoder` tanpa membengkakkan jumlah kolom.

5. **Analisis Eksplorasi Data (EDA)**
   * **Distribusi:** Variabel suhu (`MinTemp`, `MaxTemp`, `Temp9am`) memiliki bentuk distribusi yang simetris dan mendekati normal, sedangkan `Rainfall` cenderung miring ke kanan.
   * **Korelasi:** Variabel `Humidity3pm` (kelembapan jam 3 sore) terbukti menjadi indikator paling kuat terhadap potensi hujan esok hari (`RainTomorrow`).

6. **Pembagian Dataset**
   * Memisahkan variabel fitur ($X$) dan target ($y$), lalu membaginya menjadi data latih dan data uji (rasio 80:20):
     * **Data Latih (Train):** 33.251 baris
     * **Data Uji (Test):** 8.313 baris

##  Pustaka Python yang Digunakan

* **Pengolahan Data:** `pandas`, `numpy`
* **Visualisasi:** `matplotlib`, `seaborn`
* **Machine Learning & Preprocessing:** `scikit-learn` (`StandardScaler`, `LabelEncoder`, `train_test_split`)

##  Cara Menjalankan

1. **Clone repository:**
   ```bash
   git clone https://github.com/username-kamu/prediksi-hujan-australia.git
   cd prediksi-hujan-australia
   ```

2. **Install pustaka yang dibutuhkan:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

3. **Jalankan Notebook/Script:**
   Buka dan jalankan file `notebook.ipynb` untuk melihat seluruh alur pemrosesan data secara berurutan.

##  Rangkuman Singkat

| Metric / Stage | Keterangan |
| --- | --- |
| **Jumlah Data Bersih** | 41.564 baris × 23 kolom |
| **Prediktor Utama** | `Humidity3pm` |
| **Rasio Train / Test** | 80% / 20% |
| **Jumlah Data Latih** | 33.251 baris |
| **Jumlah Data Uji** | 8.313 baris |
