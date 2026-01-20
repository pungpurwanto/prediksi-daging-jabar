# 🥩 Aplikasi Prediksi Konsumsi Daging Sapi - Jawa Barat

Aplikasi berbasis web ini dirancang untuk memprediksi estimasi kebutuhan konsumsi daging sapi di Provinsi Jawa Barat. Proyek ini menggabungkan analisis data historis dari **BPS (Badan Pusat Statistik)** dengan model **Machine Learning**.

## 🚀 Fitur Utama
* **Analisis Tren:** Menampilkan pola konsumsi daging sapi dari tahun ke tahun.
* **Prediksi Interaktif:** Pengguna dapat memasukkan parameter tahun dan estimasi jumlah penduduk untuk mendapatkan proyeksi konsumsi.
* **Dashboard Sederhana:** Antarmuka yang mudah digunakan oleh pengambil kebijakan atau pelaku bisnis sektor pangan.

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python
* **Analisis Data:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Cloud

## 📋 Struktur File
* `app.py`: File utama untuk antarmuka web Streamlit.
* `model_daging_sapi.pkl`: Model Machine Learning yang telah dilatih.
* `requirements.txt`: Daftar pustaka (library) Python yang dibutuhkan.
* `data_analisis.ipynb`: Notebook proses pengolahan data di Google Colab.

## 📊 Cara Menggunakan
1. Buka aplikasi melalui link: [https://prediksi-daging-jabar.streamlit.app/]
2. Pada panel samping (sidebar), masukkan **Tahun** yang ingin diprediksi.
3. Masukkan estimasi **Jumlah Penduduk** pada tahun tersebut.
4. Klik tombol **Prediksi Sekarang**.
5. Hasil estimasi konsumsi dalam satuan Ton akan muncul di layar.

---
**Catatan:** Proyek ini dikembangkan sebagai bagian dari portofolio Data Analytics. Data yang digunakan adalah simulasi/hasil pengolahan data publik BPS.
