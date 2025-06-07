import streamlit as st
import pandas as pd
st.title('🎈 Machine Learning Projects')
st.info('Data Scientist') 
df = pd.read_csv('https://raw.githubusercontent.com/rafaelcavasani/EAD-Penguins-Dataset/refs/heads/master/penguins_size.csv')

with st.expander('Data'):
  st.write('this is pinguin classification Task')
  df = pd.read_csv('https://raw.githubusercontent.com/rafaelcavasani/EAD-Penguins-Dataset/refs/heads/master/penguins_size.csv')
  df
df['species'].value_counts().plot(kind='bar')
