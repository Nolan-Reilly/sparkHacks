from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        # user = User(username, password)
        # user.display_info()
        # login_user(user)
        # flash('Logged in successfully!', category='success')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    return '<p>Logout</p>'

@auth.route('/signup')
def signup():
    return '<p>Signup</p>'