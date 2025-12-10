# ⚡ ProductDoc AutoSuite  
AI-powered product documentation generator with a modular FastAPI backend and a Streamlit frontend.

ProductDoc AutoSuite helps teams quickly generate:
- Product requirement documents (PRDs)
- Landing page content
- FAQs
- Custom marketing copy

Built using OpenAI models, with clean modular architecture, user authentication, and history tracking.
 

---

## 🚀 Features

### 🔹 **1. Streamlit Frontend**
- Clean UI for writing a short product brief
- Adjustable depth slider for level of detail
- History panel for last 10 generations
- Responsive layout for easy demo and usage
### 🔹 **2. FastAPI Backend**
- Endpoints for:
  - `/generate` – generate PRD, FAQ, copy, scripts and marketing copy
  - `/signup` –  Register new users
  - `/login` – authenticate users  
  - `/history` – fetch last 10 generations  
- Modular architecture:
  - `main.py` → API routers  
  - `database.py` → SQLite + SQLAlchemy DB  
  - `models.py` → ORM models  
  - `prompts.py` → All prompt templates  
  - `utils.py` → reusable helpers  

### 🔹 **3. User Authentication**
- Secure password hashing using `bcrypt`
- SQLite storage for users + generation history
- Simple token-based session flow (suitable for demo and learning environments)

 ### 🔹**4. AI Integration**
 - OpenAI GPT models for all content generation
 - Centralized prompt templates for consistent outputs
 
---

##  Project Structure

productdoc_autosuite/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── prompts.py
│   ├── utils.py
│   └── routers/
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── productdoc.db
├── .env.example
├── .gitignore
└── README.md



---

## ⚙️ Installation & Setup

### 🔹 **1.Clone the repository**
git clone https://github.com/your-username/productdoc-autosuite
cd productdoc-autosuite

### 🔹 **2.Install dependencies**
pip install -r requirements.txt

### 🔹 **3.Create a .env file**
BACKEND_URL=http://localhost:8000
OPENAI_API_KEY=your_key_here

### 🔹 **4.Run the backend**
cd backend
uvicorn main:app --reload --port 8000

### 🔹 **5.Run the frontend**
cd frontend
streamlit run app.py

---

## 🔐 Authentication Flow
- User signs up with email + password
- Passwords are securely hashed using bcrypt
- Login returns a simple session token
- User ID is attached to authenticated requests
- User ID is attached to authenticated requests

---

## 🧠 Tech Stack
**Frontend**
- Streamlit
- Python

**Backend**
- FastAPI
- SQLAlchemy
- SQLite

**AI**
- OpenAI GPT models

**Security**
- bcrypt
- Environment variables via .env

---

## 🤝 Contributions

Contributions are welcome.
For major changes, please open an issue to discuss your proposal.
 



 

