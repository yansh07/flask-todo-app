from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, User, Todo
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash("Username already taken 🚩")
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered successfully ⭐")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            session['user_id'] = user.id
            flash("Logged in successfully ✅")
            return redirect(url_for('dashboard'))
        flash("Invalid credentials ⛔")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out ✔")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])  # 👈 Get the current user
    todos = Todo.query.filter_by(user_id=user.id).all()

    return render_template('dashboard.html', user=user, todos=todos)

@app.route('/add', methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    new_todo = Todo(title=title, user_id=session['user_id'])
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != session['user_id']:
        flash("Not allowed 🚫")
        return redirect(url_for('dashboard'))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)

    if request.method == 'POST':
        new_title = request.form['title']
        todo.title = new_title
        db.session.commit()
        flash("Todo updated successfully!")
        return redirect(url_for('dashboard'))

    return render_template('edit.html', todo=todo)

@app.route('/toggle/<int:id>')
def toggle(id):
    todo = Todo.query.get_or_404(id)
    
    # Optional: restrict to current user only
    if todo.user_id != session.get('user_id'):
        flash("Unauthorized access!")
        return redirect(url_for('dashboard'))
    
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('dashboard'))

