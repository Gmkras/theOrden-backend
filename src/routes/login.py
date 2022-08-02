from flask import Blueprint, redirect, render_template, request, url_for

global_login = Blueprint("login", __name__)

@global_login.route('/')
def index():
    return redirect(url_for('login.login'))

@global_login.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print(request.form['name'], request.form['password'])
        return render_template("login.html")
        
    else:
        return render_template("login.html")