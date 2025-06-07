import streamlit as st
import pandas as pd
"""st.title('🎈 Machine Learning Projects')
st.info('Data Scientist') 
df = pd.read_csv('https://raw.githubusercontent.com/rafaelcavasani/EAD-Penguins-Dataset/refs/heads/master/penguins_size.csv')

with st.expander('Data'):
  st.write('this is pinguin classification Task')
  df = pd.read_csv('https://raw.githubusercontent.com/rafaelcavasani/EAD-Penguins-Dataset/refs/heads/master/penguins_size.csv')
  df
df['species'].value_counts().plot(kind='bar')"""
import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Modern Portfolio", page_icon="💻", layout="wide")

# ستايل CSS مخصص للألوان والستايل
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #6e4aff 0%, #2d2d5a 100%);
        color: #fff;
    }
    .big-title {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #a18fff, #6e4aff, #00e0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #bdbdfc;
    }
    .section {
        background: #181830cc;
        border-radius: 18px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 32px #0002;
    }
    .icon-row img {
        margin-right: 18px;
        height: 48px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="big-title">Miladi Code</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Modern Portfolio Website</div>', unsafe_allow_html=True)

# Navigation bar simulation
nav = st.columns([1,1,1,1])
with nav[0]:
    st.markdown("**About**")
with nav[1]:
    st.markdown("**Skills**")
with nav[2]:
    st.markdown("**Projects**")
with nav[3]:
    st.markdown("**Contact**")

# Main Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("""
### 👋 Hello, There

**Providing the best Project Experience**

أنا Front-end developer عندي خبرة في تطوير الويب، الموبايل و البرمجيات. شوف شنوّا نعمل و المهارات متاعي.

[Contact Me](mailto:contact@example.com)
""")
st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("""
## 🧠 My Skills

**Designer 🟦 | Coder 🟧**

- HTML, CSS, JavaScript
- Figma, Adobe XD
- React, Next.js, MySQL

<div class="icon-row">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg"/>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Tech Stack Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("""
## 🛠️ Tech Stack

- Next.js
- HTML5
- CSS3
- JavaScript

""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("""
## 📞 Contact

- 📱 +39 111 222 444
- 📧 contact@example.com
- 🌐 [LinkedIn](https://linkedin.com)
- 🐦 [Twitter](https://twitter.com)
""")
st.markdown('</div>', unsafe_allow_html=True)
