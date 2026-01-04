import streamlit as st
import fitz  # PyMuPDF
import requests
import json

# --- Prompt Template Function ---
def generate_prompt(contract_text):
    return f"""
You are a legal expert.

Please extract the following from the lease agreement:

1. Monthly Lease Rate
2. Length of Lease Term
3. Security Deposit Amount
4. Utilities Responsibility
5. Penalties/Fees
6. Property Use

Return it in this format:
- Monthly Lease Rate:
- Lease Term:
- Security Deposit:
- Utilities:
- Penalties/Fees:
- Property Use:

Contract:
{contract_text}
"""

# --- PDF Text Extraction Function ---
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

# --- Contract Analysis Function ---
def analyze_contract(contract_text):
    prompt = generate_prompt(contract_text)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    try:
        result = response.json()["response"]
        return result
    except Exception as e:
        return f"Error analyzing contract: {e}"

# --- Streamlit App ---
st.set_page_config(page_title="AI Contract Analyzer")
st.title("📄 AI Contract Analyzer")
st.write("Upload a lease agreement and extract key legal terms using Mistral via Ollama.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        contract_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing with Mistral..."):
        analysis = analyze_contract(contract_text)

    st.subheader("🧾 Extracted Lease Terms")
    st.code(analysis, language='markdown')
