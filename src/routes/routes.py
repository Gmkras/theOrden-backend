from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)

nav = [
    {"name": "Listar Todos", "url":"/api/admin_users"},
    {"name": "negocios", "url":"/api/admin_users/1"},
]

@global_scope.route("/", methods=['GET'])
def home():
    
    parameters = {"title": "Administrador food truck",
                  "description": "crear admin"
                  }
    
    return render_template("home.html", nav=nav, **parameters)