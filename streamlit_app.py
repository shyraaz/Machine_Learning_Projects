import streamlit as st
import base64

def get_base64_video(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_file = "galaxy.mp4"  # your local video file

video_base64 = get_base64_video(video_file)

video_html = f"""
<style>
.video-background {{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    object-fit: cover;
    filter: brightness(0.7);
}}
.content {{
    position: relative;
    z-index: 1;
    color: white;
    padding: 2rem;
}}
</style>

<video autoplay muted loop class="video-background" playsinline>
    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4" />
</video>

<div class="content">
    <h1>Hello, I'm Chayma!</h1>
    <p>This is my portfolio with a local video background.</p>
</div>
"""

st.markdown(video_html, unsafe_allow_html=True)
