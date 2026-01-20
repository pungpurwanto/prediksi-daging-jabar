import streamlit as st
import joblib
import numpy as np

# 1. Judul Aplikasi
st.title("Prediksi Konsumsi Daging Sapi Jawa Barat")
st.write("Aplikasi ini memprediksi kebutuhan daging berdasarkan data BPS.")

# 2. Load Model yang tadi sudah dibuat
try:
    model = joblib.load('model_daging_sapi.pkl')
except FileNotFoundError:
    st.error("Model 'model_daging_sapi.pkl' tidak ditemukan. Pastikan model sudah disimpan.")
    st.stop()

# 3. Input Pengguna
tahun = st.number_input("Masukkan Tahun", min_value=2024, max_value=2035, value=2025)
penduduk = st.number_input("Estimasi Jumlah Penduduk (Jiwa)", value=50000000)

# 4. Tombol Prediksi
if st.button("Hitung Prediksi"):
    # Correcting input_data to match the trained model (which only uses 'tahun')
    input_data = np.array([[tahun]])

    if 'model' in locals():
        prediksi = model.predict(input_data)
        st.success(f"Estimasi Konsumsi Daging Sapi pada tahun {tahun} adalah: {prediksi[0]:,.2f} Ton")
        st.info("Catatan: Prediksi ini berdasarkan tren data historis BPS dan hanya menggunakan tahun sebagai fitur.")
    else:
        st.error("Model tidak berhasil dimuat, tidak dapat melakukan prediksi.")
