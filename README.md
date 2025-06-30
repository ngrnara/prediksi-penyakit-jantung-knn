# Prediksi Penyakit Jantung dengan Logistic Regression dan KNN

## Disusun Oleh

- **Nama**: Narakarti Nugraha  
- **NIM**: A11.2024.15787  
- **Kelompok**: A11.4404

---

## Topik / Judul

**Prediksi Penyakit Jantung dengan Logistic Regression dan KNN**

---

## Deskripsi Singkat

Dataset ini berisi 11 fitur, yaitu:

- **Age**: Umur (Numerik)
- **Sex**: Jenis kelamin (M = laki-laki, F = perempuan) (Kategorikal)
- **Chest Pain Type**: Tipe nyeri dada (NAP, ATA, ASY, TA) (Kategorikal)
- **Resting Blood Pressure**: Tekanan darah istirahat (mm Hg) (Numerik)
- **Cholesterol**: Zat lemak dalam tubuh (mg/dL) (Numerik)
- **Fasting Blood Sugar**: Kadar gula darah puasa (0 = normal, 1 = tinggi) (Biner)
- **Resting ECG**: Hasil pemeriksaan EKG saat istirahat (Kategorikal)
- **Maximum Heart Rate Achieved**: Denyut jantung maksimum (Numerik)
- **Exercise Induced Angina**: Nyeri dada saat aktivitas fisik (Kategorikal)
- **Oldpeak**: Depresi segmen ST pada EKG setelah latihan (Numerik)
- **ST Slope**: Kemiringan segmen ST pada EKG (Biner)

Label:
- **HeartDisease**: Indikasi penyakit jantung (0 = tidak, 1 = ya) (Biner)

Dataset ini digunakan untuk mendeteksi kemungkinan gagal jantung berdasarkan fitur yang ada.

---

## Masalah

Penyakit jantung adalah penyebab utama kematian di dunia, termasuk pada usia di bawah 70 tahun. Dataset ini menyediakan data untuk melatih model prediksi penyakit jantung.

---

## Tujuan

Melatih model machine learning Logistic Regression dan K-Nearest Neighbor (KNN) untuk memprediksi penyebab penyakit jantung.

---

## Penjelasan Dataset

### Atribut

- **Age**: Umur (Numerik)
- **Sex**: Jenis kelamin (M/F) (Kategorikal)
- **ChestPain**: Tipe nyeri dada (NAP, ATA, ASY, TA) (Kategorikal)
- **RestingBP**: Tekanan darah istirahat (mm Hg) (Numerik)
- **Cholesterol**: Zat lemak dalam tubuh (mg/dL) (Numerik)
- **FastingBS**: Kadar gula darah puasa (0/1) (Biner)
- **RestingECG**: Hasil pemeriksaan EKG saat istirahat (Kategorikal)
- **MaxHR**: Denyut jantung maksimum (Numerik)
- **ExerciseAngina**: Nyeri dada saat aktivitas fisik (Kategorikal)
- **Oldpeak**: Depresi segmen ST pada EKG setelah latihan (Numerik)
- **ST_Slope**: Kemiringan segmen ST pada EKG (Biner)

### Label

- **HeartDisease**: Indikasi penyakit jantung (0 = tidak, 1 = ya) (Biner)

---

## Alur / Tahapan / Kerangka Eksperimen

1. **Pengumpulan Data dan Pemahaman Data**:
   - Mengambil dataset dari Kaggle.
   - Mengeksplorasi data dengan `.head()`, `.info()`, dan `.describe()`.

2. **Preprocessing Data**:
   - Membersihkan data, menangani missing values.
   - Encoding data kategorikal dengan One-Hot Encoding.
   - Normalisasi data menggunakan Min-Max Scaling.

3. **Pemisahan Data**:
   - Membagi dataset menjadi data pelatihan (80%) dan pengujian (20%).

4. **Pemilihan Model**:
   - Melatih model Logistic Regression dan KNN menggunakan dataset.

5. **Pelatihan dan Evaluasi Model**:
   - Melatih model.
   - Mengevaluasi kinerja model dengan metrik seperti akurasi, presisi, recall, dan F1-score.

---

## Timeline Eksperimen

| Minggu Ke | Aktivitas |
|-----------|-----------|
| I | Pengumpulan Data dan Pemahaman Data |
| II | Preprocessing Data (Bagian 1): Membersihkan data |
| III | Preprocessing Data (Bagian 2): Normalisasi data |
| IV | Pemisahan Data |
| V | Pemilihan Model dan Konfigurasi |
| VI | Pelatihan dan Evaluasi Model |
| VII (Opsional) | Review, Perbaikan dan deployment ke streamlit |

---

## Sumber Dataset

[Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

## Referensi

- [Heart Disease Prediction with Logistic Regression and KNN](https://github.com/RizkyAdhiNugroho/heart-disease-prediction-with-Logistic-Regression-KNN)

- link Streamlit (https://data-mining-prediksi-penyakit-jantung-menggunakan-logistik-reg.streamlit.app/)
- link Streamlit KNN ([prediksi-penyakit-jantung-knn ∙ main ∙ app.py](https://prediksi-penyakit-jantung-knn.streamlit.app/))
