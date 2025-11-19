from flask import Flask
from flask_wtf.csrf import CSRFProject

app = Flask(__name__)

csrf = CSRFProject()
csrf.init_app(app)

from application import routes


