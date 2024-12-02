import streamlit as st
import pandas as pd

# Fungsi untuk memuat data dari CSV
@st.cache_data
def load_data():
    try:
        # Ganti dengan lokasi file CSV Anda
        data = pd.read_csv("pln_clean.csv", 
                           names=["Title", "Date", "Link", "Content", "Category"],
                           encoding="utf-8")
        data["Date"] = pd.to_datetime(data["Date"])  # Konversi ke format datetime
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Fungsi untuk membuat kategori berita PESTEL
def filter_by_category(data, category):
    return data[data["Category"].str.lower() == category.lower()]

# Load data
data = load_data()

# Judul Dashboard
st.title("Dashboard Berita PESTEL Analysis")
st.write("**Platform Analisis Berita Berdasarkan PESTEL Framework**")
st.write("Menampilkan berita relevan berdasarkan kategori: **Political, Economic, Social, Technological, Environmental, Legal (PESTEL)**.")

# Tab berdasarkan kategori PESTEL
tabs = st.tabs(["Political", "Economic", "Social", "Technological", "Environmental", "Legal"])

categories = ["Political", "Economic", "Social", "Technological", "Environmental", "Legal"]

# Loop untuk membuat tab per kategori
for tab, category in zip(tabs, categories):
    with tab:
        st.subheader(f"Kategori: {category}")
        
        # Filter berita berdasarkan kategori
        category_data = filter_by_category(data, category)
        
        # Tampilkan pesan jika tidak ada data
        if category_data.empty:
            st.info(f"Tidak ada berita di kategori {category}.")
        else:
            # Loop untuk menampilkan berita
            for index, row in category_data.iterrows():
                st.markdown(f"### {row['Title']}")
                st.markdown(f"**Tanggal**: {row['Date'].strftime('%Y-%m-%d %H:%M:%S')}")
                st.markdown(f"**Link**: [Baca selengkapnya]({row['Link']})")
                st.markdown(f"**Konten**: {row['Content'][:200]}...")  # Tampilkan cuplikan konten
                st.markdown("---")  # Garis pemisah antar berita
