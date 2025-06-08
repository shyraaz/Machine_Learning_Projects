import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Chiraze Feriani Portfolio", page_icon="✨")

# === Load Background ===
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: url('data:image/png;base64,{}') no-repeat center center fixed;
    background-size: cover;
}
</style>
"""



# === Hero Section ===
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("<h1 style='font-size: 6rem; color: #ff89ff;'>C<br>F</h1>", unsafe_allow_html=True)
with col2:
    st.markdown("""
    ## 👋 Hello! I'm **Chayma Farhat**
    ### 💻 Full Stack Developer — Crafting Digital Experiences
    I build innovative web applications with cutting-edge technologies, focusing on **performance**, **accessibility**, and **stunning user experiences**.
    
    [👉 View My Work](#featured-projects) | [📬 Get In Touch](#contact)
    """, unsafe_allow_html=True)

# === Featured Projects ===
st.markdown("## 🚀 Featured Projects", unsafe_allow_html=True)

projects = [
    {
        "title": "CreativAize",
        "desc": "Unleash your creativity without breaking the bank! Free AI image generation with no limits.",
        "tags": ["Next.js", "AI", "Image Generation", "Creative Tool"],
    },
    {
        "title": "Co-Bee",
        "desc": "A gamified education platform where teachers create fun team quizzes and students earn stars.",
        "tags": ["Next.js", "ShadCN", "Education", "Quiz", "Multiplayer"],
    },
    {
        "title": "First Parc",
        "desc": "Smart park management app for cities and organizations using Flutter.",
        "tags": ["Flutter", "Mobile", "Park Management"],
    },
]

for project in projects:
    st.markdown(f"""
    ### {project['title']}
    {project['desc']}
    **Tech:** {", ".join(project['tags'])}
    """)

# === Toolkit Section ===
st.markdown("## 🧰 My Toolkit")

toolkit = {
    "Frontend": ["HTML", "CSS3", "Bootstrap", "Angular", "Next.js", "Flutter", "React", "Tailwind CSS"],
    "Backend": ["Node.js", "ASP.NET Core", "Symfony", "Spring Boot", "REST API", "SOAP API"],
    "Programming": ["C", "C#", "Java", "Python", "TypeScript", "JavaScript", "Dart", "PHP"],
    "Data": ["SQL", "PL/SQL", "MongoDB", "Redis", "Firebase", "Hadoop"],
    "Tools": ["Visual Studio", "VS Code", "Eclipse", "Android Studio", "IntelliJ", "Google Colab", "Power BI"],
    "Deployment": ["GitHub", "Vercel", "Netlify", "Cloudinary"],
}

cols = st.columns(3)
i = 0
for category, tools in toolkit.items():
    with cols[i % 3]:
        st.markdown(f"### {category}")
        for tool in tools:
            st.markdown(f"- {tool}")
    i += 1

# === About Section ===
st.markdown("## 👩‍💻 Profile: About Me")
st.markdown("""
I'm a full-stack developer passionate about creating impactful web and mobile applications.  
I recently completed my degree in **Applied Information Technology**, and I'm excited to dive into projects that push my skills forward.

When I'm not coding, you'll find me exploring new technologies, blogging about my experiences, or enhancing my skills through certifications like **Digital Marketing**.
""")

# === Contact Section ===
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("## 📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! I'll get back to you soon 😊")

# === Footer ===
st.markdown("---")
cols = st.columns([1, 4, 1])
with cols[1]:
    st.markdown("© 2025 Chayma Farhat. All rights reserved.")
    st.markdown("[GitHub](https://github.com) | [LinkedIn](https://linkedin.com)")

