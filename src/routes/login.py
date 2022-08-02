from flask import Blueprint, redirect, render_template, request, url_for, flash

from ..controller import admin_users_controller
from ..models.models import Admin_users

global_login = Blueprint("login", __name__)

@global_login.route('/')
def index():
    return redirect(url_for('login.login'))

@global_login.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = Admin_users(0,request.form['name'],request.form['password'])
        logged_user = Admin_users.login(user)
        if logged_user != None:
            if logged_user.password:
                return redirect('home.html')
            else:
                flash('invalid password')
                return render_template("login.html")
        else:
            flash('User not found')
            return render_template("login.html")
    else:
        return render_template("login.html")
