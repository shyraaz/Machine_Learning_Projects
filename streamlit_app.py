import streamlit as st

st.set_page_config(page_title="Modern Portfolio", page_icon="💻", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    [data-testid="stHeader"], .st-emotion-cache-18ni7ap {
        display: none; 
    }
    .stApp {
        background: linear-gradient(135deg, #6e4aff, #2d2d5a) !important;
        color: white;
    }
    .big-title {
        font-size: 3.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #a18fff, #6e4aff, #00e0ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: white;
    }
    .section {
        background-color: #ffffff10;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 32px #0002;
    }
    .icon-row img {
        margin: 0 10px;
        height: 48px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 32px;">
    <a href="#about" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none;">About</a>
    <a href="#skills" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none;">Skills</a>
    <a href="#projects" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none;">Projects</a>
    <a href="#contact" style="padding:10px 24px; background:#6e4aff; color:#fff; border-radius:8px; text-decoration:none;">Contact</a>
</div>
""", unsafe_allow_html=True)

# === Introduction Section ===
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="big-title">Hello, I\'m Chiraze Feriani</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="subtitle">
        I am a Junior Data Scientist passionate about data, technology, and creative problem-solving.
        I love uncovering hidden patterns and transforming numbers into real-world solutions.
        With experience in data analysis, AI, and smart project development, I'm always eager to learn, grow, and take on new challenges! 🚀
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712107.png", width=300)  # You can change this to any DS-themed image URL

# === Skills Section ===
st.markdown('<div class="section" id="skills">', unsafe_allow_html=True)
st.markdown("## 🧠 My Skills")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    - **Languages**: Python  
    - **AI & ML**: Machine Learning, Deep Learning  
    - **Tools**: Streamlit, TensorFlow  
    """)
with col2:
    st.markdown("""
    <div class="icon-row">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
        <img src="https://img.icons8.com/ios/50/4e8cff/brain--v1.svg"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"/>
        <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"/>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# === Projects Section ===
st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)
st.markdown("## 🛠️ Tech Stack")
st.markdown("""
- **Web**: Next.js, HTML5, CSS3, JavaScript
- **Data**: Pandas, NumPy, Matplotlib
""")
st.markdown("</div>", unsafe_allow_html=True)

# === Contact Section with Form ===
st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
st.markdown("## 📞 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you! Your message has been received.")

st.markdown("</div>", unsafe_allow_html=True)
