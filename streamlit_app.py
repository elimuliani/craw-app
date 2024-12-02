import streamlit as st
import pandas as pd

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    try:
        # Membaca file CSV
        data = pd.read_csv("pln_clean.csv", encoding="utf-8")
        
        # Debug: Periksa kolom yang ada di dataset
        st.write("Kolom dalam dataset:", data.columns.tolist())
        
        # Periksa apakah kolom yang diharapkan ada
        expected_columns = ["headline", "date", "link", "content_text", "category"]
        for col in expected_columns:
            if col not in data.columns:
                st.warning(f"Kolom '{col}' tidak ditemukan. Periksa file CSV Anda.")
        
        # Normalisasi data (pastikan kolom 'category' ada)
        if "category" in data.columns:
            data["category"] = data["category"].str.strip().str.lower()  # Normalisasi kategori
        else:
            st.error("Kolom 'category' tidak ada dalam dataset.")
            st.stop()

        # Konversi tanggal jika ada kolom 'date'
        if "date" in data.columns:
            data["date"] = pd.to_datetime(data["date"], errors="coerce")
        
        return data
    except Exception as e:
        st.error(f"Error saat memuat data: {e}")
        return pd.DataFrame()

# Fungsi untuk memfilter berita berdasarkan kategori
def filter_by_category(data, category):
    if "category" not in data.columns:
        st.warning("Kolom 'category' tidak ditemukan dalam data.")
        return pd.DataFrame()
    return data[data["category"] == category.lower()]

# Memuat data
data = load_data()

# Judul aplikasi
st.title("Dashboard PESTEL Analysis")
st.write("Dashboard ini menampilkan berita berdasarkan kategori PESTEL (Political, Economic, Social, Technological, Environmental, Legal).")

# Tabs untuk setiap kategori PESTEL
tabs = st.tabs(["Political", "Economic", "Social", "Technological", "Environmental", "Legal"])
categories = ["political", "economic", "social", "technological", "environmental", "legal"]

# Menampilkan berita di setiap kategori
for tab, category in zip(tabs, categories):
    with tab:
        st.subheader(f"Kategori: {category.capitalize()}")
        
        # Filter data berdasarkan kategori
        category_data = filter_by_category(data, category)
        
        # Jika tidak ada data
        if category_data.empty:
            st.info(f"Tidak ada berita di kategori {category.capitalize()}.")
        else:
            # Menampilkan berita
            for _, row in category_data.iterrows():
                st.markdown(f"### {row['headline']}")
                st.markdown(f"**Tanggal**: {row['date'].strftime('%Y-%m-%d %H:%M:%S')}" if pd.notnull(row["date"]) else "Tanggal tidak tersedia")
                st.markdown(f"**Link**: [Baca selengkapnya]({row['link']})")
                st.markdown(f"**Konten**: {row['content_text'][:200]}...")
                st.markdown("---")
