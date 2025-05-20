from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jsr123XELR&LJERsecurekey'

    socketio.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app