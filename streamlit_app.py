import streamlit as st

st.set_page_config(page_title="Modern Portfolio", page_icon="💻", layout="wide")

# ستايل CSS للخلفية فقط (ما نبدلوش لون النص العام)
st.markdown(
    """
    <style>
     /* نخبيو header متاع Streamlit */
    [data-testid="stHeader"] {
        display: none;
    }
    /* نخبيو الـ toolbar متاع Streamlit Cloud */
    .st-emotion-cache-18ni7ap {
        display: none !important;
    }
    .stApp {
        background: linear-gradient(135deg, #6e4aff 0%, #2d2d5a 100%) !important;
    }
    
    .big-title {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #a18fff, #6e4aff, #00e0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-size: 0.5rem;
        color: white;
    }
    .section {
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

# Navbar عصري بالأزرار (HTML)
st.markdown("""
<div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 32px;">
    <a href="#about" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none; font-weight:bold;">About</a>
    <a href="#skills" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none; font-weight:bold;">Skills</a>
    <a href="#projects" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none; font-weight:bold;">Projects</a>
    <a href="#contact" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none; font-weight:bold;">Contact</a>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="big-title" id="about">Hello, There</div>',
            unsafe_allow_html=True)
st.markdown("""<div class="big-title"> 
I am Chiraze Feriani, passionate about data, 
technology, and creative 
problem-solving. I love uncovering hidden patterns and transforming numbers
into real-world solutions. With experience in data analysis, AI, and smart
project development, Im always eager to learn, grow, and take on 
new challenges! 🚀</div>""", unsafe_allow_html=True)

# Main Section
st.markdown('<div class="subtitle"></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section" id="skills">', unsafe_allow_html=True)
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
st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)
st.markdown("""
## 🛠️ Tech Stack

- Next.js
- HTML5
- CSS3
- JavaScript

""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
st.markdown("""
## 📞 Contact

- 📱 +39 111 222 444
- 📧 contact@example.com
- 🌐 [LinkedIn](https://linkedin.com)
- 🐦 [Twitter](https://twitter.com)
""")
st.markdown('</div>', unsafe_allow_html=True)

