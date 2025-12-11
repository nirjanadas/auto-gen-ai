import os
import time
import json
from typing import Optional

import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

# Config
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
ADMIN_BYPASS = os.getenv("ADMIN_BYPASS", "False").lower() in ("1", "true", "yes")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")
REQUEST_TIMEOUT = 10


# Helpers: backend wrappers
def backend_available() -> bool:
    try:
        r = requests.get(f"{BACKEND_URL}/health", timeout=3)
        return r.status_code == 200
    except Exception:
        return False


def backend_signup(email: str, password: str) -> (bool, str):
    try:
        r = requests.post(
            f"{BACKEND_URL}/signup",
            json={"email": email, "password": password},
            timeout=REQUEST_TIMEOUT,
        )
        if r.status_code in (200, 201):
            return True, "Account created successfully."
        else:
            data = r.json() if r.headers.get("content-type", "").startswith("application/") else {}
            msg = data.get("detail", r.text[:200])
            return False, f"Signup failed: {msg}"
    except Exception as e:
        return False, f"Signup error: {e}"


def backend_login(email: str, password: str) -> (bool, Optional[str], str):
    try:
        r = requests.post(
            f"{BACKEND_URL}/login",
            json={"email": email, "password": password},
            timeout=REQUEST_TIMEOUT,
        )
        if r.status_code == 200:
            data = r.json()
            token = data.get("token") or data.get("access_token") or data.get("detail")
            return True, token, "Logged in"
        else:
            data = r.json() if r.headers.get("content-type", "").startswith("application/") else {}
            msg = data.get("detail", r.text[:200])
            return False, None, f"Login failed: {msg}"
    except Exception as e:
        return False, None, f"Login error: {e}"


def backend_generate(token: Optional[str], brief: str, depth: int):
    payload = {"brief": brief, "depth": depth}
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    r = requests.post(f"{BACKEND_URL}/generate", json=payload, headers=headers, timeout=REQUEST_TIMEOUT * 4)
    r.raise_for_status()
    return r.json()


def backend_history(token: Optional[str]):
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    r = requests.get(f"{BACKEND_URL}/history", headers=headers, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    return r.json()


# Demo fallback outputs
def demo_generate(brief: str, depth: int):
    brief_short = brief.strip()[:120]
    output = {
        "PRD": f"Demo PRD for: {brief_short}\n\n(Replace with backend for real AI results.)",
        "Landing Page": f"{brief_short} — headline, subtext, features & CTA.",
        "FAQ": "\n".join([f"Q{i+1}: Example question?\nA: Example answer."
                           for i in range(5 if depth < 3 else 10)]),
    }
    time.sleep(0.7)
    return output


def demo_history():
    return []


# Authentication & session
def init_session_state():
    for key in ["token", "user_email", "last_generation", "history"]:
        if key not in st.session_state:
            st.session_state[key] = None


def developer_auto_login_if_enabled():
    if ADMIN_BYPASS and ADMIN_EMAIL:
        st.session_state["token"] = "DEV-BYPASS-TOKEN"
        st.session_state["user_email"] = ADMIN_EMAIL
        st.sidebar.success(f"Developer mode: logged in as {ADMIN_EMAIL}")


# Sidebar login/signup
def login_signup_sidebar():
    st.sidebar.header("Account")

    if ADMIN_BYPASS and ADMIN_EMAIL:
        st.sidebar.info("Developer bypass enabled (.env)")
        if st.sidebar.button("Logout (dev)"):
            st.session_state["token"] = None
            st.session_state["user_email"] = None
        return True

    if st.session_state["token"]:
        st.sidebar.success(f"Logged in as {st.session_state['user_email']}")
        if st.sidebar.button("Logout"):
            st.session_state["token"] = None
            st.session_state["user_email"] = None
        return True

    tab_login, tab_signup = st.sidebar.tabs(["Login", "Sign up"])

    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            if not email or not password:
                st.warning("Please enter email and password.")
            else:
                if backend_available():
                    ok, token, msg = backend_login(email, password)
                    if ok and token:
                        st.session_state["token"] = token
                        st.session_state["user_email"] = email
                        st.success("Logged in successfully.")
                    else:
                        st.error(msg)
                else:
                    st.error("Backend unavailable.")

    with tab_signup:
        new_email = st.text_input("New email", key="signup_email")
        new_password = st.text_input("New password", type="password", key="signup_password")

        if st.button("Sign up"):
            if not new_email or not new_password:
                st.warning("Please enter email and password.")
            else:
                if backend_available():
                    ok, msg = backend_signup(new_email, new_password)
                    if ok:
                        st.success("Account created. Please log in.")
                    else:
                        st.error(msg)
                else:
                    st.error("Backend unavailable.")

    return st.session_state.get("token") is not None


# Main app
def main():
    st.set_page_config(page_title="AutoGen AI", layout="wide")
    st.title("AutoGen AI")
    st.caption("AI-powered generator for PRDs, landing pages, FAQs, and marketing content.")

    init_session_state()
    developer_auto_login_if_enabled()

    backend_ok = backend_available()

    if backend_ok:
        st.info(f"Backend available: {BACKEND_URL}")
    else:
        st.warning("Backend offline — using demo mode.")

    logged_in = login_signup_sidebar()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Write product brief")
        brief = st.text_area("Product brief", height=150,
                             placeholder="Example: AI tool for helping businesses create content automatically.")

        depth = st.slider("Detail level", 1, 3, 2)

        if st.button("Generate"):
            if not brief.strip():
                st.warning("Please enter a brief.")
            else:
                with st.spinner("Generating..."):
                    if backend_ok:
                        try:
                            res = backend_generate(st.session_state["token"], brief, depth)
                        except Exception:
                            res = demo_generate(brief, depth)
                    else:
                        res = demo_generate(brief, depth)

                    st.session_state["last_generation"] = res
                    st.success("Done!")

        if st.session_state["last_generation"]:
            st.markdown("### Results")
            for section_name, content in st.session_state["last_generation"].items():
                st.markdown(f"**{section_name}**")
                st.write(content)

    with col2:
        st.subheader("History (last 10)")
        history_displayed = False

        if backend_ok:
            try:
                history = backend_history(st.session_state["token"])
                st.session_state["history"] = history

                if history:
                    for item in history:
                        brief_text = item.get("brief", "—")
                        created = item.get("created_at", "")
                        st.markdown(f"- **{brief_text}** — {created}")

                    history_displayed = True
                else:
                    st.info("No history yet.")

            except Exception:
                pass

        if not history_displayed:
            st.info("History unavailable (demo mode).")

        st.markdown("---")
        st.subheader("Quick tips")
        st.write(
            """
            • Use a short 1–2 line brief  
            • Depth 3 = more detailed content  
            • Offline mode uses demo output  
            """
        )

    st.markdown("---")
    st.caption("Dev mode available via BACKEND_URL and ADMIN_BYPASS in .env")


if __name__ == "__main__":
    main()
