

import streamlit as st
import requests

st.set_page_config(page_title="email writer", layout="wide")

st.title("📧 email writer")

# ---- Job Input ----
st.subheader("Job Details")
url = st.text_input("Enter Job URL")

# ---- Sender Details ----
st.subheader("Your Details")
name = st.text_input("Your Name", value="Muhammad Abdullah")
role = st.text_input("Your Role", value="Founder / CEO")
company = st.text_input("Company Name", value="Tensorsoft")

# ---- Optional Enhancements ----
tone = st.selectbox(
    "Email Tone",
    ["Professional", "Friendly", "Persuasive"]
)
details =  st.text_area(
    "Enter Company Details (e.g., name, industry, size, website)",
    value="Tensorsoft, Tech/AI, 10-50 employees, https://tensorsoft.ai",
    height=100)
# ---- Generate Button ----
if st.button("Generate Email"):
    if not url:
        st.warning("Please enter a job URL")
    else:
        with st.spinner("Generating email..."):
            res = requests.post(
                "http://127.0.0.1:8000/generate-emails",
                json={
                    "url": url,
                    "sender": {
                        "name": name,
                        "role": role,
                        "company": company
                        
                    },
                    "tone": tone,
                    "company_details": details,
                }
            )

        if res.status_code == 200:
            st.success("Email generated successfully!")
            for email in res.json()["emails"]:
                st.code(email, language="markdown")
        else:
            st.error(res.text)
