import streamlit as st
import pandas as pd

# Fungsi untuk memuat data dari CSV
@st.cache_data
def load_data(file_path):
    try:
        # Membaca file CSV
        data = pd.read_csv(file_path)

        # Debug: Tampilkan kolom yang ditemukan
        st.write("Kolom dalam dataset:", data.columns.tolist())

        # Periksa kolom yang diharapkan
        expected_columns = ["headline", "date", "link", "content_text", "category"]
        missing_columns = [col for col in expected_columns if col not in data.columns]
        if missing_columns:
            st.error(f"Kolom berikut tidak ditemukan dalam dataset: {missing_columns}")
            st.stop()

        # Normalisasi kolom kategori
        data["category"] = data["category"].str.strip().str.lower()  # Standarisasi huruf kecil
        return data
    except Exception as e:
        st.error(f"Error saat memuat data: {e}")
        return pd.DataFrame()

# Path ke file CSV
file_path = "pln_clean.csv"

# Memuat data
data = load_data(file_path)

# Judul dashboard
st.title("Dashboard Analisis PESTEL")
st.write("Menampilkan berita berdasarkan kategori PESTEL: Political, Economic, Social, Technological, Environmental, Legal.")

# Tabs untuk kategori PESTEL
tabs = st.tabs(["Political", "Economic", "Social", "Technological", "Environmental", "Legal"])
categories = ["political", "economic", "social", "technological", "environmental", "legal"]

# Menampilkan berita berdasarkan kategori
for tab, category in zip(tabs, categories):
    with tab:
        st.subheader(f"Kategori: {category.capitalize()}")

        # Filter data berdasarkan kategori
        category_data = data[data["category"] == category]

        if category_data.empty:
            st.info(f"Tidak ada berita untuk kategori {category.capitalize()}.")
        else:
            for _, row in category_data.iterrows():
                st.markdown(f"### {row['headline']}")
                st.markdown(f"**Tanggal**: {row['date']}")
                st.markdown(f"**Link**: [Baca selengkapnya]({row['link']})")
                st.markdown(f"**Konten**: {row['content_text'][:200]}...")
                st.markdown("---")
