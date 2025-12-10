# 🚀 ProductDoc AutoSuite  
### AI-powered tool to generate PRDs, landing page copy, FAQs & short video scripts

ProductDoc AutoSuite is an end-to-end AI application that helps startups, founders and product teams generate high-quality product documentation instantly.  
It includes a **FastAPI backend**, **Streamlit frontend**, **secure user login**, and **OpenAI-powered generation workflows**.

---

## ⭐ Features

### 🔐 User Authentication
- Secure login system  
- SQLite database with hashed passwords (bcrypt)  
- Clean session management  

### 🧠 AI Content Generation
- Generates:
  - Product requirement documents (PRDs)  
  - Landing page copy  
  - Marketing FAQ  
  - Short video script  
- Uses OpenAI GPT models  
- Adjustable depth (detail level slider)

### 📡 FastAPI Backend
- REST API for:
  - `/signup`
  - `/login`
  - `/generate`
  - `/history`
- Clean modular backend (database, models, prompts, utils)

### 🎨 Streamlit Frontend
- Modern UI for input, generation, and history  
- Developer mode fallback (runs without backend)  
- Auto-login for developer using `.env`  

### 🗂 Database
- SQLite used for:
  - Users  
  - Generation history  
- Lightweight + portable

---

## 🏗 Tech Stack

| Layer | Technologies |
|-------|--------------|
| Frontend | Streamlit |
| Backend | FastAPI, Uvicorn |
| Database | SQLite, SQLAlchemy |
| Auth | bcrypt password hashing |
| AI | OpenAI GPT models |
| Other | python-dotenv, requests |

---
productdoc_autosuite/
│── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── prompts.py
│ ├── utils.py
│
│── frontend/
│ ├── app.py
│
│── productdoc.db
│── requirements.txt
│── .env.example
│── README.md
## 📁 Project Structure

