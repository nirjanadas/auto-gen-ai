import streamlit as st
import requests

API_BASE = "https://productdoc-autosuite.onrender.com"
GENERATE_URL = f"{API_BASE}/generate"
HISTORY_URL = f"{API_BASE}/history"

st.set_page_config(page_title="ProductDoc AutoSuite", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #1f2933, #020617);
        color: #e5e7eb;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #22d3ee, #a855f7, #f97316);
        -webkit-background-clip: text;
        color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #cbd5f5;
        margin-bottom: 1.5rem;
    }
    .glass-card {
        background: rgba(15,23,42,0.85);
        border-radius: 18px;
        padding: 1.5rem 1.8rem;
        border: 1px solid rgba(148,163,184,0.35);
        box-shadow: 0 18px 45px rgba(15,23,42,0.9);
    }
    .stButton>button {
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        border-radius: 999px;
        padding: 0.5rem 1.8rem;
        border: none;
        font-weight: 600;
        font-size: 0.98rem;
        box-shadow: 0 10px 25px rgba(22,163,74,0.35);
    }
    .stButton>button:hover {
        filter: brightness(1.08);
        box-shadow: 0 16px 35px rgba(22,163,74,0.55);
    }
    .stSlider > div[data-baseweb="slider"] > div {
        background: linear-gradient(90deg, #f97316, #ec4899, #22d3ee);
    }
    textarea, .stTextArea textarea {
        background-color: #020617 !important;
        border-radius: 12px !important;
        border: 1px solid #475569 !important;
        color: #e5e7eb !important;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        color: #e5e7eb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- HEADER ----------
st.markdown(
    """
    <div class="glass-card" style="margin-bottom: 1.5rem;">
        <div class="main-title">ProductDoc AutoSuite</div>
        <div class="subtitle">
            Turn a short product idea into a PRD, landing page, FAQ, and video script template – powered by AI.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- LAYOUT ----------
left, right = st.columns([1, 1.4])

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("### 🧠 Product Brief")
    brief = st.text_area(
        "Write product brief here (2–3 lines)",
        label_visibility="collapsed",
        height=150,
        placeholder="Example: AI tool that helps small businesses create marketing content automatically using templates.",
    )
    depth = st.slider("Depth (detail level)", 1, 3, 2)

    generate_clicked = st.button("Generate")

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    # --------- NEW GENERATION OUTPUT ---------
    if generate_clicked:
        if not brief.strip():
            st.error("Please write a brief first 🙂")
        else:
            with st.spinner("✨ Generating your document pack..."):
                try:
                    resp = requests.post(GENERATE_URL, json={"brief": brief, "depth": depth})
                except Exception as e:
                    st.error(f"Could not reach backend: {e}")
                else:
                    if resp.status_code == 200:
                        data = resp.json()

                        st.markdown('<div class="section-title">📘 PRD</div>', unsafe_allow_html=True)
                        st.text_area("PRD", data.get("PRD", ""), height=160, label_visibility="collapsed")

                        st.markdown('<div class="section-title">📣 Landing Page</div>', unsafe_allow_html=True)
                        st.text_area("Landing Page", data.get("Landing Page", ""), height=160, label_visibility="collapsed")

                        st.markdown('<div class="section-title">❓ FAQ</div>', unsafe_allow_html=True)
                        st.text_area("FAQ", data.get("FAQ", ""), height=160, label_visibility="collapsed")

                        st.markdown('<div class="section-title">🎬 Video Script Template</div>', unsafe_allow_html=True)
                        st.text_area(
                            "Video Script",
                            data.get("Video Script", ""),
                            height=200,
                            label_visibility="collapsed",
                        )
                    else:
                        st.error(f"Backend error {resp.status_code}: {resp.text}")
    else:
        st.markdown(
            "<p style='color:#9ca3af;'>Fill the brief on the left and click <b>Generate</b> to see your documents here.</p>",
            unsafe_allow_html=True,
        )

    # --------- HISTORY SECTION ---------
    st.markdown('<div class="section-title">📚 History (last 10)</div>', unsafe_allow_html=True)

    try:
        hist_resp = requests.get(HISTORY_URL)
        if hist_resp.status_code == 200:
            history = hist_resp.json()
            if history:
                options = [
                    f"{item['id']} | {item['brief'][:40]}..."
                    for item in history
                ]
                selected = st.selectbox(
                    "Select a past generation",
                    ["-- Select --"] + options,
                )

                if selected != "-- Select --":
                    idx = options.index(selected)
                    chosen = history[idx]
                    docs = chosen.get("documents", {})

                    st.write("### 🔁 Previously generated")
                    st.text_area(
                        "PRD (saved)",
                        docs.get("PRD", ""),
                        height=120,
                        label_visibility="collapsed",
                    )
                    st.text_area(
                        "Landing Page (saved)",
                        docs.get("Landing Page", ""),
                        height=120,
                        label_visibility="collapsed",
                    )
                    st.text_area(
                        "FAQ (saved)",
                        docs.get("FAQ", ""),
                        height=120,
                        label_visibility="collapsed",
                    )
                    st.text_area(
                        "Video Script (saved)",
                        docs.get("Video Script", ""),
                        height=150,
                        label_visibility="collapsed",
                    )
            else:
                st.write("No history yet. Generate something first 🙂")
        else:
            st.write("Could not load history from backend.")
    except Exception as e:
        st.write(f"Error loading history: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
