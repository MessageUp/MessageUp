from flask import Flask
import sqlite3
from flask_bootstrap import Bootstrap
from service.db import DB

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "VERY_SECRET_KEY"

db = DB()


from service import views
