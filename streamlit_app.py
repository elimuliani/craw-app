import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset yang sudah dibersihkan
data = pd.read_csv('pln_cleaned.csv')

# Judul aplikasi web
st.title("Analisis PESTEL untuk PT PLN")

# Tampilkan dataset
st.write("Tabel Data Analisis:")
st.dataframe(data)

# Buat grafik distribusi kategori PESTEL
st.write("Grafik Distribusi Kategori PESTEL")
plt.figure(figsize=(8, 6))
sns.countplot(x='PESTEL_category', data=data, palette='viridis')
plt.title('Distribusi Kategori PESTEL')
st.pyplot(plt)

# Buat grafik distribusi sentimen
st.write("Grafik Distribusi Sentimen")
plt.figure(figsize=(8, 6))
sns.countplot(x='Sentiment', data=data, palette='coolwarm')
plt.title('Distribusi Sentimen Secara Keseluruhan')
st.pyplot(plt)

