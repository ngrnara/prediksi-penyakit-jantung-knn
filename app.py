import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- KONFIGURASI TAMPILAN APLIKASI ---
st.set_page_config(
    page_title="Prediksi Penyakit Jantung Menggunakan KNN",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)



# --- FUNGSI UNTUK MEMUAT MODEL (DENGAN CACHING AGAR CEPAT) ---
# Caching akan menyimpan model di memori agar tidak perlu di-load ulang
@st.cache_resource
def load_model(model_path):
    """Fungsi untuk memuat model dari file .pkl"""
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Error: File model tidak ditemukan di path '{model_path}'. Pastikan file model ada di folder yang sama dengan app.py.")
        return None

# --- FUNGSI UTAMA APLIKASI ---
def main():
    # Memuat model KNN yang sudah dilatih
    model = load_model('model_knn_terbaik.pkl')
    
    # Jangan lanjutkan jika model gagal di-load
    if model is None:
        return

    # --- TAMPILAN ANTARMUKA (UI) STREAMLIT ---
    # Membuat dua kolom utama
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("❤️ Aplikasi Prediksi Penyakit Jantung")
        st.write(
            "Penyakit jantung adalah salah satu penyebab utama kematian di seluruh dunia. Prediksi risiko penyakit jantung secara dini dapat membantu dalam pengambilan keputusan medis yang tepat waktu."
            "Aplikasi ini membantu memprediksi risiko penyakit jantung pada pasien "
            "menggunakan model Machine Learning **KNN (K-Nearest Neighbors)**. "
            "Masukkan data medis pasien di panel sebelah kanan untuk melihat hasilnya."
        )
        st.info(
            "Model ini dilatih berdasarkan data 'Heart Failure Prediction' dari Kaggle "
            "dan memiliki **akurasi sekitar 89%** pada data uji."
        )
        
        st.header("Hasil Prediksi")
        # Placeholder untuk hasil prediksi
        result_placeholder = st.empty()
        result_placeholder.info("Hasil prediksi akan muncul di sini setelah Anda menekan tombol 'Lakukan Prediksi'.")
    
    # --- PANEL INPUT DI SEBELAH KANAN (SIDEBAR) ---
    with st.sidebar:
        st.header("Masukkan Data Pasien:")

        # --- Membuat Form Input ---
        with st.form("prediction_form"):
            # Input data pasien
            Age = st.number_input("Umur", min_value=20, max_value=100, value=50)
            
            Sex = st.selectbox("Jenis Kelamin", (1, 0), format_func=lambda x: 'Pria' if x == 1 else 'Wanita')
            
            cp_options = {0: "Asymptomatic", 1: "Atypical Angina", 2: "Non-Anginal Pain", 3: "Typical Angina"}
            ChestPainType = st.selectbox("Tipe Nyeri Dada", options=list(cp_options.keys()), format_func=lambda x: f"{x} - {cp_options.get(x, 'N/A')}")
            
            RestingBP = st.number_input("Tekanan Darah Istirahat (mmHg)", min_value=80, max_value=220, value=120)
            
            Cholesterol = st.number_input("Kolesterol (mg/dl)", min_value=0, max_value=600, value=200)
            
            FastingBS = st.selectbox("Gula Darah Puasa > 120 mg/dl?", (1, 0), format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
            
            ecg_options = {0: "Normal", 1: "ST-T Abnormality", 2: "LVH"}
            RestingECG = st.selectbox("Hasil EKG Istirahat", options=list(ecg_options.keys()), format_func=lambda x: ecg_options[x])
            
            MaxHR = st.number_input("Detak Jantung Maksimum", min_value=60, max_value=220, value=150)
            
            ExerciseAngina = st.selectbox("Nyeri Dada saat Olahraga?", (1, 0), format_func=lambda x: 'Ya' if x == 1 else 'Tidak')

            Oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

            slope_options = {0: "Upsloping", 1: "Flat", 2: "Downsloping"}
            ST_Slope = st.selectbox("Kemiringan Segmen ST", options=list(slope_options.keys()), format_func=lambda x: slope_options[x])

            # Tombol Submit
            submit_button = st.form_submit_button(label="Lakukan Prediksi")

    # --- LOGIKA SETELAH TOMBOL DITEKAN ---
    if submit_button:
        input_data = {
            'Age': Age, 'Sex': Sex, 'ChestPainType': ChestPainType, 'RestingBP': RestingBP,
            'Cholesterol': Cholesterol, 'FastingBS': FastingBS, 'RestingECG': RestingECG,
            'MaxHR': MaxHR, 'ExerciseAngina': ExerciseAngina, 'Oldpeak': Oldpeak, 'ST_Slope': ST_Slope
        }
        input_df = pd.DataFrame([input_data])
        
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)
        prob_berisiko = prediction_proba[0][1]

        # Hapus placeholder dan tampilkan hasil
        result_placeholder.empty()
        if prediction[0] == 1:
            st.warning(f"**Pasien Berisiko Terkena Penyakit Jantung**", icon="⚠️")
        else:
            st.success(f"**Pasien Tidak Berisiko Terkena Penyakit Jantung**", icon="✅")
        
        st.metric(label="Tingkat Probabilitas Risiko", value=f"{prob_berisiko:.2%}")
        
        with st.expander("Lihat Detail Data yang Dimasukkan"):
            st.write(input_data)

# --- MENJALANKAN FUNGSI UTAMA ---
if __name__ == '__main__':
    main()