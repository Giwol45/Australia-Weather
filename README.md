#  Prediksi Hujan Australia

Repository ini berisi seluruh alur pembersihan data, analisis eksploratif (EDA), hingga penyiapan data untuk memprediksi apakah besok akan turun hujan berdasarkan data cuaca harian di Australia.

##  Ringkasan Proyek

Tujuan utama dari alur kerja ini adalah menyiapkan data yang bersih dan siap pakai untuk pemodelan *machine learning*.

* **Ukuran Data Akhir:** 41.564 baris × 23 kolom
* **Variabel Target:** `RainTomorrow` (Klasifikasi: Ya / Tidak)

##  liblary Python yang Digunakan

* **Pengolahan Data:** `pandas`, `numpy`
* **Visualisasi:** `matplotlib`, `seaborn`
* **Machine Learning & Preprocessing:** `scikit-learn` (`StandardScaler`, `LabelEncoder`)

##  Rangkuman Singkat

| Metric / Stage | Keterangan |
| --- | --- |
| **Jumlah Data Bersih** | 41.564 baris × 23 kolom |
| **Prediktor Utama** | `Humidity3pm` |
| **Rasio Train / Test** | 80% / 20% |
| **Jumlah Data Latih** | 33.251 baris |
| **Jumlah Data Uji** | 8.313 baris |
