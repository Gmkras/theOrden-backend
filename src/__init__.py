from flask import Flask
import werkzeug
from config import Config
from flask_cors import CORS
from .database.admin_users import reset_table
from werkzeug.security import generate_password_hash

from .routes import global_scope, api_scope, errors_scope, global_login

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

app.config.from_object(Config)

CORS(app)

app.register_blueprint(global_login, url_prefix='/')
app.register_blueprint(global_scope, url_prefix='/home')
app.register_blueprint(errors_scope, url_prefix='/home')
app.register_blueprint(api_scope, url_prefix='/api')
