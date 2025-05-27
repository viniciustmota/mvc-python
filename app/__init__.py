import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

path = os.getcwd()
template_dir=os.path.abspath(os.path.join(path, os.pardir))

template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object('config')

db = SQLAlchemy(app)
from .models import book_model, author_model
from .services import book_service, author_service
from .controlers import book_controler, author_controler