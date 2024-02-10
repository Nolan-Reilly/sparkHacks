from flask import Blueprint, render_template, request, flash, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .object import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

def findInFile(filename, username, password):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            x = lines[i].split()
            if x[0] == username and check_password_hash(x[1], password):
                return User(username, password)
    return None

# Login page backend
@auth.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # read in username and password from login.html
        username = request.form.get('username')
        password = request.form.get('password')
        user = findInFile('user.txt', username, password)
        if user:
            login_user(user)
            return redirect(url_for('index.index'))
        else:
            flash("Incorrect username or password. Try again...")
    return render_template("login.html", user=current_user)

# Logout page backend
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Signup page backend
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # read in username and password from signup.html
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username, generate_password_hash(password, method='pbkdf2'))
        user.write_to_file('user.txt')
        login_user(user)
        return redirect(url_for('index.index'))
    return render_template("signup.html", user=current_user)