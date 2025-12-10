# ⚡ ProductDoc AutoSuite  
AI-powered product documentation generator with a modular FastAPI backend and a Streamlit-based frontend.

ProductDoc AutoSuite helps teams quickly generate:
- Product requirement documents (PRDs)
- Landing page content
- FAQs
- Short video scripts
- Custom marketing copy

The app uses OpenAI models and provides a clean developer experience with modular APIs, user login, and history storage.

---

## 🚀 Features

### 🔹 **1. Streamlit Frontend**
- Clean UI for writing a short product brief
- Adjustable depth slider (detail level)
- History panel for last 10 generations
- Developer bypass mode (auto-login for devs)

### 🔹 **2. FastAPI Backend**
- Endpoints for:
  - `/generate` – generate PRD, FAQ, copy, scripts  
  - `/signup` – create an account  
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
- JWT-free simple token/session pattern (for demo scale)

### 🔹 **4. Developer Mode**
The frontend allows a special mode if defined in `.env`:

ADMIN_BYPASS=yes
ADMIN_EMAIL=your@email.com

yaml
Copy code

This logs the developer in automatically and bypasses auth when the backend is offline.

### 🔹 **5. Graceful Offline Mode**
If backend is unreachable:
- The frontend switches to *demo generation outputs*
- History becomes unavailable
- The UI continues to work for demonstration

This ensures the project can be showcased even without full server deployment.

---

## 📁 Project Structure

productdoc_autosuite/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── prompts.py
│ ├── utils.py
│ └── pycache/
│
├── frontend/
│ ├── app.py (Streamlit app)
│
├── requirements.txt
├── productdoc.db
├── .gitignore
├── .env.example
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/productdoc-autosuite
cd productdoc-autosuite
2️⃣ Install requirements
(You do NOT need pinned versions — normal install works fine.)

bash
Copy code
pip install -r requirements.txt
3️⃣ Create a .env file
env
Copy code
BACKEND_URL=http://localhost:8000
OPENAI_API_KEY=your_key_here

# Optional dev auto-login
ADMIN_BYPASS=yes
ADMIN_EMAIL=youremail@example.com
4️⃣ Run backend (FastAPI)
bash
Copy code
cd backend
uvicorn main:app --reload --port 8000
5️⃣ Run frontend (Streamlit)
bash
Copy code
cd frontend
streamlit run app.py
🔐 Authentication Flow
User signs up (email + password)

Passwords are hashed using bcrypt

User logs in

Authenticated requests include the user’s ID

History is tied to the specific user

Developer mode bypasses login (via .env)

🧠 Tech Stack
Frontend
Streamlit

Python

Backend
FastAPI

SQLAlchemy

SQLite

AI
OpenAI GPT models

Security
bcrypt

.env environment variables

Git ignored secrets

📌 Why this project is strong for hiring
This project demonstrates:

✔ Full-stack ability (API + frontend)
✔ Modular backend architecture
✔ Authentication system (bcrypt + SQLite)
✔ Prompt engineering
✔ Real AI integration using OpenAI
✔ Clean code structure
✔ Modern frameworks: FastAPI + Streamlit
✔ Deployable & scalable structure

Perfect for SDE, AI Engineer, ML Engineer, and Full-Stack Python roles.

🤝 Contributions
Pull requests are welcome.
For major changes, please open an issue first to discuss.

