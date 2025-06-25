# pages/1_Keterangan_Dataset.py

import streamlit as st

st.set_page_config(page_title="Keterangan Dataset", page_icon="📖")

st.title("📖 Keterangan Dataset")
st.markdown("---")
st.write("Halaman ini berisi penjelasan untuk setiap fitur medis yang digunakan sebagai input dalam model prediksi.")

# Penjelasan untuk setiap fitur
st.header("Fitur Demografis")
st.markdown("**Age (Umur):** Umur pasien dalam satuan tahun.")
st.markdown("**Sex (Jenis Kelamin):** Jenis kelamin pasien (Pria atau Wanita).")

st.header("Fitur Klinis & Hasil Tes")
st.markdown("**RestingBP (Tekanan Darah Istirahat):** Tekanan darah sistolik saat pasien sedang beristirahat, diukur dalam mmHg.")
st.markdown("**Cholesterol (Kolesterol):** Kadar kolesterol serum total, diukur dalam mg/dl.")
st.markdown("**FastingBS (Gula Darah Puasa):** Menunjukkan apakah kadar gula darah puasa pasien di atas 120 mg/dl (Ya) atau tidak (Tidak).")

st.header("Fitur Hasil Elektrokardiogram (EKG)")
st.markdown("""
**ChestPainType (Tipe Nyeri Dada):**
- **Typical Angina:** Nyeri dada yang khas disebabkan oleh penyakit jantung koroner.
- **Atypical Angina:** Nyeri dada yang tidak sepenuhnya khas angina.
- **Non-Anginal Pain:** Nyeri dada yang kemungkinan besar bukan berasal dari jantung.
- **Asymptomatic:** Pasien tidak menunjukkan gejala nyeri dada.
""")
st.markdown("""
**RestingECG (Hasil EKG Istirahat):**
- **Normal:** Hasil EKG tidak menunjukkan kelainan signifikan.
- **ST-T Abnormality:** Ditemukan kelainan pada gelombang ST-T (bisa menandakan masalah ringan).
- **LVH (Left Ventricular Hypertrophy):** Menunjukkan adanya penebalan pada ventrikel kiri jantung.
""")
st.markdown("""
**ExerciseAngina (Nyeri saat Olahraga):** Menunjukkan apakah pasien mengalami angina (nyeri dada) saat melakukan aktivitas fisik (Ya) atau tidak (Tidak).
""")
st.markdown("""
**ST_Slope (Kemiringan Segmen ST):** Pola kemiringan segmen ST pada EKG saat puncak latihan.
- **Upsloping:** Menanjak, umumnya dianggap normal.
- **Flat:** Datar, sering dikaitkan dengan iskemia atau masalah jantung.
- **Downsloping:** Menurun, sering dianggap sebagai indikator kuat masalah jantung.
""")
st.markdown("**Oldpeak:** Nilai depresi segmen ST yang diukur pada EKG saat latihan dibandingkan saat istirahat.")
st.markdown("**MaxHR (Detak Jantung Maksimum):** Detak jantung tertinggi yang berhasil dicapai pasien selama tes latihan.")