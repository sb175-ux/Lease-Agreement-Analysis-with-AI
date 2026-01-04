# AI-Contract-Analyzer
AI-Powered Contract Analyzer using Mistral 7B LLM

## Overview
The **AI Contract Analyzer** is a Python-based offline legal document analyzer designed to simplify and automate the review of real estate lease agreements. It extracts key clauses, summarizes obligations, and flags potential risks using **Mistral 7B** LLM run locally via **Ollama**, ensuring full data privacy.

This tool was developed as part of a capstone project for the **MS in Business Analytics / MIS program at the University at Buffalo** under the course *Applied AI for Managers (MGS-636)*.

---

## 🚀 Features
- 📑 **Clause Extraction**: Identifies rent terms, deposits, lease duration, utilities, penalties, and property usage.
- 🧠 **LLM-Powered Summarization**: Uses prompt engineering with Mistral 7B to extract and return key lease details.
- 🔐 **Privacy-Focused**: Entirely offline—no cloud-based processing.
- ⚡ **Fast & Lightweight**: Local model inference ensures speed and security.

---

## 🏗️ Architecture

### 🔧 Technologies Used
- [Ollama](https://ollama.com): Local LLM runner  
- [Mistral 7B](https://mistral.ai): Language model for legal text understanding  
- Python (Streamlit, PyMuPDF, Requests)

### 🔄 Workflow
1. User uploads lease agreement (PDF).
2. PyMuPDF extracts raw text.
3. Prompt template guides Mistral to extract specific terms.
4. Structured response displayed to the user in Streamlit.

---

## 🛠️ How to Run Locally

### ⚙️ Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Mistral model pulled: `ollama pull mistral`

### 📥 Installation
```bash
git clone https://github.com/yourusername/ai-contract-analyzer.git
cd ai-contract-analyzer
pip install -r requirements.txt
```
---

## 📚 Learnings & Challenges

Parsing PDFs with inconsistent layouts required preprocessing.

Prompt tuning was critical for consistent outputs.

Running offline LLMs proved efficient and privacy-friendly.

---

## 🔮 Future Enhancements
Highlight key clauses directly on PDFs.

Compare multiple contracts side-by-side.

Support additional legal contract types (e.g., service or employment agreements).

Integrate fine-tuned legal LLMs (e.g., CUAD dataset).

## Connect with me?

[LinkedIn](https://www.linkedin.com/in/sagar-naduvinkeri/)

snaduvin@buffalo.edu
