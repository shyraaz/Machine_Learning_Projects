import streamlit as st
import base64

def video_base64(file_path): 
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_b64 = video_base64("background.mp4")

video_html = f"""
<video autoplay muted loop playsinline
    style="
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        object-fit: cover;
        filter: brightness(0.7);
        z-index: -1;
    ">
    <source src="data:video/mp4;base64,{video_b64}" type="video/mp4" />
    Your browser does not support the video tag.
</video>

<div style="position: relative; z-index: 1; color: white; padding: 2rem;">
    <h1>Hello, I'm Chiraze !</h1>
    <p>This is my portfolio with a local video background.</p>
</div>
"""

st.components.v1.html(video_html, height=700, scrolling=False)
