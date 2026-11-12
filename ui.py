from urllib.parse import urlparse

import streamlit as st

from youtubevideo_analyzer import youtubeAnalyzer


st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 10% 0%, rgba(108, 72, 220, 0.18), transparent 38%),
            #0b1020;
        color: #f3f4f8;
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    .block-container {
        max-width: 1050px;
        padding-top: 3rem;
        padding-bottom: 2rem;
    }
    .hero {
        padding: 2.2rem 2.4rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        background: linear-gradient(120deg, rgba(28, 35, 62, 0.96), rgba(20, 25, 45, 0.92));
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.24);
    }
    .eyebrow {
        color: #b7a5ff;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    .hero h1 {
        margin: 0.55rem 0 0.65rem;
        color: #ffffff;
        font-size: clamp(2rem, 5vw, 3.2rem);
        letter-spacing: -0.045em;
    }
    .hero p {
        max-width: 650px;
        margin: 0;
        color: #b9c0d4;
        font-size: 1.05rem;
        line-height: 1.65;
    }
    [data-testid="stForm"] {
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        background: rgba(19, 25, 44, 0.9);
    }
    [data-testid="stTextInput"] input {
        min-height: 3rem;
        border-radius: 12px;
        background: #101629;
    }
    [data-testid="stFormSubmitButton"] button {
        min-height: 3rem;
        border: 0;
        border-radius: 12px;
        background: linear-gradient(100deg, #7657e8, #a052d7);
        color: #ffffff;
        font-weight: 700;
        transition: filter 0.2s ease, transform 0.2s ease;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        filter: brightness(1.12);
        transform: translateY(-1px);
    }
    .hint {
        margin-top: 0.65rem;
        color: #929bb2;
        font-size: 0.88rem;
    }
    .footer {
        padding-top: 2rem;
        color: #77819a;
        font-size: 0.82rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="hero">
        <div class="eyebrow">Watch less. Understand more.</div>
        <h1>YouTube Video Analyzer</h1>
        <p>Turn a video into a clear, useful breakdown of its key ideas, insights, and takeaways.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.form("video_analysis_form"):
    video_url = st.text_input(
        "YouTube video link",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste a YouTube video URL to get started.",
    )
    submitted = st.form_submit_button("Analyze video  →", use_container_width=True)

st.markdown(
    '<div class="hint">Works with youtube.com and youtu.be links.</div>',
    unsafe_allow_html=True,
)

if submitted:
    parsed_url = urlparse(video_url.strip())
    hostname = (parsed_url.hostname or "").lower()
    if hostname not in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}:
        st.error("Enter a valid YouTube video link to continue.")
    else:
        with st.spinner("Watching the video and preparing your analysis..."):
            try:
                agent = youtubeAnalyzer()
                response = agent.run(f"Analyze this video: {video_url.strip()}")
                analysis = response.content
                if isinstance(analysis, str) and analysis.strip():
                    st.subheader("Your video analysis")
                    st.markdown(analysis)
                else:
                    st.warning("The analysis completed, but no text was returned. Please try again.")
            except Exception as exc:
                st.error(f"Video analysis failed: {exc}")

st.markdown('<div class="footer">Made for curious minds.</div>', unsafe_allow_html=True)
