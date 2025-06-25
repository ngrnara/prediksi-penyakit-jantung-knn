# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# --- KONFIGURASI TAMPILAN APLIKASI ---
st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNGSI UNTUK MEMUAT DAN MELATIH MODEL ---
@st.cache_resource
def get_trained_model():
    """Melatih model KNN dan menyimpannya di cache."""
    try:
        data = pd.read_csv('datasets-heartnew1.csv')
    except FileNotFoundError:
        return None # Akan ditangani di UI utama

    X = data.drop('HeartDisease', axis=1)
    y = data['HeartDisease']
    numerical_features = X.columns.tolist()
    preprocessor = ColumnTransformer(transformers=[('num', StandardScaler(), numerical_features)])
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', KNeighborsClassifier(n_neighbors=7))
    ])
    model_pipeline.fit(X, y)
    return model_pipeline

# Memuat model
model = get_trained_model()

# --- TAMPILAN UTAMA APLIKASI ---
st.title("❤️ Prediksi Risiko Penyakit Jantung")
st.markdown("---")
st.markdown("""
Penyakit jantung adalah salah satu penyebab utama kematian di seluruh dunia. Prediksi risiko penyakit jantung secara dini dapat membantu dalam pengambilan keputusan medis yang tepat waktu.

Aplikasi ini dirancang untuk membantu praktisi kesehatan dan pasien dalam memprediksi kemungkinan risiko penyakit jantung berdasarkan data medis. Model yang digunakan adalah **KNN (K-Nearest Neighbors)** dengan akurasi **~89%**.
""")

# --- PANEL SAMPING (SIDEBAR) UNTUK INPUT DATA ---
with st.sidebar:
    st.header("Masukkan Data Pasien:")
    
    with st.form("prediction_form"):
        # Input data pasien
        Age = st.number_input("Umur", 20, 100, 50)
        Sex = st.selectbox("Jenis Kelamin", ("Pria", "Wanita"))
        
        cp_options = {"Typical Angina": 3, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 0}
        chest_pain_text = st.selectbox("Tipe Nyeri Dada", options=cp_options.keys())
        
        RestingBP = st.number_input("Tekanan Darah Istirahat (mmHg)", 80, 220, 120)
        Cholesterol = st.number_input("Kolesterol (mg/dl)", 0, 600, 200)
        FastingBS = st.selectbox("Gula Darah Puasa > 120 mg/dl?", ("Ya", "Tidak"))

        ecg_options = {"Normal": 1, "ST-T Abnormality": 2, "LVH": 0}
        resting_ecg_text = st.selectbox("Hasil EKG Istirahat", options=ecg_options.keys())
        
        MaxHR = st.number_input("Detak Jantung Maksimum", 60, 220, 150)
        ExerciseAngina = st.selectbox("Nyeri Dada saat Olahraga?", ("Ya", "Tidak"))
        Oldpeak = st.number_input("Oldpeak (Depresi ST)", -3.0, 10.0, 1.0, step=0.1)
        
        slope_options = {"Upsloping": 2, "Flat": 1, "Downsloping": 0}
        st_slope_text = st.selectbox("Kemiringan Segmen ST", options=slope_options.keys())

        submit_button = st.form_submit_button(label="Lakukan Prediksi")

# --- MENAMPILKAN HASIL DI HALAMAN UTAMA ---
st.header("Hasil Prediksi")
if not submitted:
    st.info("Silakan isi data pasien di panel samping dan klik 'Lakukan Prediksi' untuk melihat hasilnya.")

if submitted:
    if model is None:
        st.error("Model tidak berhasil dimuat karena file 'datasets-heartnew1.csv' tidak ditemukan. Pastikan file tersebut ada di repository GitHub Anda.")
    else:
        # Konversi input teks ke angka
        input_data = pd.DataFrame({
            "Age": [Age], "Sex": [1 if Sex == "Pria" else 0],
            "ChestPainType": [cp_options[chest_pain_text]], "RestingBP": [RestingBP],
            "Cholesterol": [Cholesterol], "FastingBS": [1 if FastingBS == "Ya" else 0],
            "RestingECG": [ecg_options[resting_ecg_text]], "MaxHR": [MaxHR],
            "ExerciseAngina": [1 if ExerciseAngina == "Ya" else 0], "Oldpeak": [Oldpeak],
            "ST_Slope": [slope_options[st_slope_text]]
        })
        
        # Lakukan prediksi
        try:
            prediction = model.predict(input_data)[0]
            prediction_proba = model.predict_proba(input_data)[0][1]

            if prediction == 1:
                st.warning(f"**Pasien Berisiko Terkena Penyakit Jantung**", icon="⚠️")
            else:
                st.success(f"**Pasien Tidak Berisiko Terkena Penyakit Jantung**", icon="✅")
            
            st.metric(label="Tingkat Probabilitas Risiko", value=f"{prediction_proba:.2%}")
            
            with st.expander("Lihat Detail Data yang Dimasukkan"):
                st.dataframe(input_data)
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")

# Disclaimer
st.markdown("---")
st.caption("Disclaimer: Aplikasi ini adalah alat bantu prediksi dan tidak menggantikan diagnosis medis profesional. Selalu konsultasikan dengan dokter untuk evaluasi kesehatan yang akurat.")