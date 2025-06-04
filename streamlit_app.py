import streamlit as st
import pandas as pd
st.title('🎈 Machine Learning Projects')
st.info('Data Scientist') 
with st.expander('Data'):
  st.write('this is pinguin classification Task')
  df = pd.read_csv('https://raw.githubusercontent.com/rafaelcavasani/EAD-Penguins-Dataset/refs/heads/master/penguins_size.csv')
  df
  df['Adelie'].values_count().plot(kind='bar')
