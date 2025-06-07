import streamlit as st
import pandas as pd

st.set_page_config(page_title="Modern Portfolio", page_icon="💻", layout="wide")
# ستايل CSS مخصص للألوان والستايل (من غير فيديو)
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)






# Header
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("About"):
        st.write("🧑‍💼 هذا القسم متاع About")
with col2:
    if st.button("Skills"):
        st.write("🛠️ هذا القسم متاع Skills")
with col3:
    if st.button("Projects"):
        st.write("📚 هذا القسم متاع Projects")
with col4:
    if st.button("Contact"):
        st.write("📞 هذا القسم متاع Contact")
st.markdown("""
### 👋 Hello, There)        
st.markdown('<div class="big-title"> Hello, There </div>', unsafe_allow_html=True)
st.markdown('<div class="big-title">i am a Data Scientist </div>', unsafe_allow_html=True)

# Navigation bar (أزرار في صف واحد)


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
