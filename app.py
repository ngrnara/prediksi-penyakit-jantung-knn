import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Menggunakan cache agar model hanya dilatih sekali saat aplikasi pertama kali dijalankan
@st.cache_resource
def get_trained_model():
    """
    Fungsi ini akan memuat data, mendefinisikan preprocessor, 
    dan melatih model Logistic Regression.
    """
    # 1. Muat dataset Anda
    try:
        data = pd.read_csv('datasets-heartnew1.csv')
    except FileNotFoundError:
        st.error("File dataset 'datasets-heartnew1.csv' tidak ditemukan.")
        return None

    # 2. Pisahkan fitur (X) dan target (y)
    X = data.drop('HeartDisease', axis=1)
    y = data['HeartDisease']

    # 3. Definisikan preprocessor (ini adalah langkah yang hilang di skrip Anda)
    # Model yang baik harus dilatih pada data yang di-scaling
    numerical_features = X.columns.tolist() # Semua fitur di data Anda adalah numerik
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features)
        ]
    )

    # 4. Buat pipeline yang menggabungkan preprocessing dan model
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(random_state=42, max_iter=1000))
    ])

    # 5. Latih model dengan seluruh data yang ada
    model_pipeline.fit(X, y)
    
    return model_pipeline

# Panggil fungsi untuk mendapatkan model yang sudah siap pakai
model = get_trained_model()

# --- BAGIAN ANTARMUKA (UI) STREAMLIT ---
# (Bagian ini diambil dari skrip Anda dan sedikit disempurnakan)

st.title("Prediksi Penyakit Jantung")
st.write("Aplikasi ini memprediksi risiko penyakit jantung menggunakan model Logistic Regression.")

st.header("Input Data Pasien")

# Input data dibuat dalam form agar lebih rapi
with st.form("input_form"):
    # Menggunakan kolom agar tata letak lebih baik
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Umur", min_value=1, max_value=120, value=50)
        sex = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
        # Mapping untuk Tipe Nyeri Dada (ChestPainType)
        cp_options = {"Typical Angina": 3, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 0}
        chest_pain_text = st.selectbox("Jenis Nyeri Dada", options=list(cp_options.keys()))
        
        resting_bp = st.number_input("Tekanan Darah Saat Istirahat (mmHg)", min_value=50, max_value=220, value=120)
        cholesterol = st.number_input("Kolesterol (mg/dL)", min_value=0, max_value=600, value=200)
        fasting_bs = st.selectbox("Gula Darah Puasa > 120 mg/dL", ["Ya", "Tidak"])

    with col2:
        # Mapping untuk Hasil EKG Istirahat (RestingECG)
        ecg_options = {"Normal": 1, "ST-T Abnormality": 2, "LVH": 0}
        resting_ecg_text = st.selectbox("Hasil EKG Saat Istirahat", options=list(ecg_options.keys()))
        
        max_hr = st.number_input("Detak Jantung Maksimum", min_value=60, max_value=220, value=150)
        exercise_angina = st.selectbox("Angina Selama Latihan", ["Ya", "Tidak"])
        oldpeak = st.number_input("Depresi ST (Oldpeak)", min_value=-3.0, max_value=10.0, value=1.0, step=0.1)
        
        # Mapping untuk Kemiringan Segmen ST (ST_Slope)
        slope_options = {"Upsloping": 2, "Flat": 1, "Downsloping": 0}
        st_slope_text = st.selectbox("Kemiringan Segmen ST", options=list(slope_options.keys()))

    # Tombol submit
    submitted = st.form_submit_button("Prediksi")

if submitted:
    if model:
        # Konversi input teks dari pengguna menjadi angka sesuai format dataset Anda
        input_data = pd.DataFrame({
            "Age": [age],
            "Sex": [1 if sex == "Pria" else 0],
            "ChestPainType": [cp_options[chest_pain_text]],
            "RestingBP": [resting_bp],
            "Cholesterol": [cholesterol],
            "FastingBS": [1 if fasting_bs == "Ya" else 0],
            "RestingECG": [ecg_options[resting_ecg_text]],
            "MaxHR": [max_hr],
            "ExerciseAngina": [1 if exercise_angina == "Ya" else 0],
            "Oldpeak": [oldpeak],
            "ST_Slope": [slope_options[st_slope_text]]
        })

        st.subheader("Data yang Anda Masukkan:")
        st.write(input_data)
        
        try:
            # Lakukan prediksi
            prediction = model.predict(input_data)[0]
            prediction_proba = model.predict_proba(input_data)[0][1] # Probabilitas kelas 1

            st.subheader("Hasil Prediksi")
            if prediction == 1:
                st.error(f"Pasien Berisiko Terkena Penyakit Jantung (Probabilitas: {prediction_proba:.2%})")
            else:
                st.success(f"Pasien Tidak Berisiko Terkena Penyakit Jantung (Probabilitas Risiko: {prediction_proba:.2%})")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
    else:
        st.error("Model belum siap digunakan.")