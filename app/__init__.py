from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
    user = db.engine.url.username
    password = db.engine.url.password

    print(f"Usuario: {user}, Contraseña: {password}")