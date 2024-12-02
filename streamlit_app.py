import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("pln_clean.csv") 

# Fungsi untuk membuat plot berdasarkan kategori
def plot_category(category):
    st.write(f"## Kategori: {category}")
    cols = [col for col in df.columns if category.lower() in col.lower()]
    df_category = df[cols]
    
    # Contoh visualisasi: Histogram
    for col in df_category.columns:
        fig, ax = plt.subplots()
        sns.histplot(data=df_category, x=col, kde=True)
        st.pyplot(fig)

# Sidebar untuk memilih kategori
st.sidebar.title("Pilih Kategori PESTEL")
category = st.sidebar.selectbox("", ["Politik", "Ekonomi", "Sosial", "Teknologi", "Lingkungan", "Legal"])

# Tampilkan plot berdasarkan pilihan
plot_category(category)
