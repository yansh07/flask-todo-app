# ToDo App
## A minimal and responsive ToDo web application built using Flask, Bootstrap, PostgreSQL (Supabase), and Render for full-stack deployment.
## 🚀 Live Demo
👉 [View Live App](https://flask-todo-app-7cqt.onrender.com)

---

## ✨ Features

- User Authentication (Register & Login)
- Create, Edit, and Delete ToDos
- Mark tasks as completed
- Data stored in PostgreSQL (via Supabase)
- Responsive UI with HTML/CSS (or Bootstrap)
- Deployed on Render (Free Tier)

---

## 🛠 Tech Stack

| Category     | Tools Used                       |
|--------------|-----------------------------------|
| Backend      | Flask, Python                     |
| Frontend     | Jinja2 templates, HTML, CSS       |
| Database     | PostgreSQL (Supabase)             |
| Deployment   | Render.com                        |
| ORM          | SQLAlchemy                        |

---

## 📁 Project Structure  
/project-root
│
├── app.py # Main Flask app  
├── requirements.txt  
├── templates/ # HTML files (login, home, etc.)  
│ ├── login.html  
│ ├── register.html  
│ └── home.html  
├── static/ # (Optional) CSS / JS files  
└── ...  


---

> ⚠️ Note: Data is stored on a free-tier Supabase DB, which may reset occasionally.

---

## 📦 Setup Instructions (For Local)

```bash
# 1. Clone repo
git clone https://github.com/yourusername/flask-todo-app.git

# 2. Navigate to folder
cd flask-todo-app

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

📌 Notes  
The app is hosted on Render using Gunicorn
Supabase Free Plan is used (no expiry warnings as of now)
Aimed at portfolio/demo usage — not production-secure

---

## Made with 💙 by [Priyanshu](https://github.com/yansh07)  

---
**• Developed a full-stack ToDo web application using Flask and PostgreSQL with complete user authentication (login/register).**  
**• Integrated Supabase as a remote PostgreSQL backend, handling all CRUD operations for ToDos.**  
**• Deployed the app on Render with a production WSGI setup using Gunicorn, achieving a fully live web interface.**  
**• Implemented secure session handling and organized Jinja2 templates for a clean, responsive UI.**  
**• Built for portfolio use with scalable architecture and database hosted on a Free Tier cloud platform.**  
