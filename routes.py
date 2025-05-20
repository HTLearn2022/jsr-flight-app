from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

socketio = SocketIO()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jsr123XELR&LJERSecurekey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
