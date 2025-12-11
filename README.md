## 🖼️ UI Preview

![AUTOGEN UI](assets/ui_preview.png)


---

# ⚡ AutoGen AI  
AI-powered product documentation generator with a modular FastAPI backend and a Streamlit frontend.

AutoGen AI converts a short product brief into high-quality outputs:
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

      Endpoints
      - `/generate` – generate PRD, FAQ, landing page content, marketing copy 
      - `/signup` – register users  
      - `/login` – authenticate users  
      - `/history` – recent 10 generations  

      Modular Architecture
      - `main.py` → API routers  
      - `database.py` → SQLite + SQLAlchemy DB  
      - `models.py` → ORM models  
      - `prompts.py` → prompt templates  
      - `utils.py` → helper utilities  

### 🔹 **3. User Authentication**
- Secure password hashing using `bcrypt`
- SQLite storage for users + generation history
- Simple token-based session flow (suitable for demo and learning environments)

 ### 🔹**4. AI Integration**
 - OpenAI GPT models for all content generation
 - Centralized prompt templates for consistent outputs
 
---

##  📁 Project Structure

 <pre>
auto_gen_ai/
│
├── assets
|    ├── ui_preview.png
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
├── README.md
└── LICENSE
  
</pre>


---

## 🧱 Clean Architecture (Visual Overview)

   ```text
───────────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────────────┐
│ PRESENTATION LAYER        (UI - Streamlit)                                   │
│                                                                              │
│   • frontend/app.py                                                          │
└──────────────────────────────▲───────────────────────────────────────────────┘
                               │
                               │
───────────────────────────────|───────────────────────────────────────────────
                               │
┌─────────────────────────────────────────────────────────────────────────────┐
│ APPLICATION / USE CASES LAYER                                               │
│                                                                             │
│   • backend/main.py     • backend/prompts.py     • backend/utils.py         │
└──────────────────────────────▲──────────────────────────────────────────────┘
                               │
                               │
───────────────────────────────|───────────────────────────────────────────────
                               │
┌──────────────────────────────────────────────────────────────────────────────┐
│ DOMAIN LAYER               (Business Entities)                               │
│                                                                              │
│   • backend/models.py                                                        │
└──────────────────────────────▲───────────────────────────────────────────────┘
                               │
                               │
───────────────────────────────|────────────────────────────────────────────────
                               │
┌───────────────────────────────────────────────────────────────────────────────┐
│ INFRASTRUCTURE LAYER                                                          │
│                                                                               │
│   • backend/database.py                                                       |
└───────────────────────────────────────────────────────────────────────────────┘

---

## ⚙️ Installation & Setup

### 🔹 **1.Clone the repository**
```git clone https://github.com/nirjanadas/autogen-ai.git```
```cd autogen-ai```

### 🔹 **2.Install dependencies**
```pip install -r requirements.txt```

### 🔹 **3.Create a .env file**
```BACKEND_URL=http://localhost:8000```
```OPENAI_API_KEY=your_key_here```

### 🔹 **4.Run the backend**
```cd backend```
```uvicorn main:app --reload --port 8000```

### 🔹 **5.Run the frontend**
```cd frontend```
```streamlit run app.py```

---

## 🔐 Authentication Flow
- User signs up with email + password
- Passwords are securely hashed using bcrypt
- Login returns a simple session token
- User ID is attached to authenticated requests
- User ID is attached to authenticated requests

---

## 🧠 Tech Stack

<div align="center">

### 🖥️ **Frontend**
| Technology | Purpose |
|-----------|----------|
| 🎨 Streamlit | UI & user interaction |
| 🐍 Python | Core language |

### ⚙️ **Backend**
| Technology | Purpose |
|-----------|----------|
| 🚀 FastAPI | API framework |
| 🏗️ SQLAlchemy | ORM & database layer |
| 🗄️ SQLite | Lightweight database |

### 🤖 **AI**
| Technology | Purpose |
|-----------|----------|
| 🔮 OpenAI GPT Models | Content generation |

### 🔐 **Security**
| Technology | Purpose |
|-----------|----------|
| 🔑 bcrypt | Password hashing |
| 🧩 .env Config | Secure environment variables |

</div>


---

## 🤝 Contributions

Contributions are welcome.
For major changes, please open an issue to discuss your proposal.
 



 

