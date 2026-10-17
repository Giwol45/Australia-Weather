# Prediksi Hujan Australia

alur lengkap pembersihan data, analisis eksploratif (EDA), *preprocessing*, hingga *deployment* model *machine learning* sederhana menggunakan API Flask untuk memprediksi apakah besok akan turun hujan berdasarkan historis data cuaca harian di Australia.

## Ringkasan Proyek

Tujuan utama dari proyek ini adalah mengolah data mentah cuaca Australia hingga siap digunakan untuk pelatihan model klasifikasi, lalu menyediakannya dalam bentuk REST API agar bisa menerima masukan data baru.

- **Ukuran Data Akhir (Bersih):** 41.564 baris × 23 kolom
- **Variabel Target:** `RainTomorrow` (Klasifikasi Biner: Ya / Tidak)
- **Prediktor Utama:** `Humidity3pm` (Kelembapan jam 3 sore)

## Rangkuman Data & Pembagian Dataset

| Metric / Stage | Keterangan |
| --- | --- |
| **Jumlah Data Bersih** | 41.564 baris × 23 kolom |
| **Rasio Split Train / Test** | 80% / 20% |
| **Jumlah Data Latih (Train)** | 33.251 baris |
| **Jumlah Data Uji (Test)** | 8.313 baris |

## Tech Stack & Library Python

- **Pengolahan & Analisis Data:** `pandas`, `numpy`
- **Visualisasi Data:** `matplotlib`, `seaborn`
- **Machine Learning & Preprocessing:** `scikit-learn` (`StandardScaler`, `LabelEncoder`, DLL)
- **Deployment & Service:** `Flask`

## Alur Preprocessing & Pembersihan Data

1. **Penanganan Missing Values:**
   - Kolom dengan persentase *missing value* di atas 75% dieliminasi.
   - Kolom numerik sisanya diimputasi menggunakan nilai **median**.
   - Kolom kategorikal diimputasi menggunakan nilai **modus**.
2. **Encoding & Feature Scaling:**
   - Variabel kategorikal diubah menjadi numerik menggunakan `LabelEncoder` / *One-Hot Encoding*.
   - Feature scaling diterapkan menggunakan `StandardScaler` agar distribusi variabel seimbang sebelum masuk ke model.
3. **Pembagian Dataset:**
   - Data dipisah dengan rasio 80:20 untuk *train* dan *test set*.

## Testing Prediction Endpoint

Kamu bisa melakukan tes prediksi dengan mengirimkan request HTTP POST ke endpoint `/predict` menggunakan cURL:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @data.json
```

**Contoh Response:**
```json
{
  "prediction": [0]
}
```
*Catatan: Nilai `0` berarti diprediksi **Tidak Hujan** (`No`), sedangkan `1` berarti diprediksi **Hujan** (`Yes`).*
