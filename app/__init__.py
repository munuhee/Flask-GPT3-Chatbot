from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile('config.py')
socketio = SocketIO(app)

from app.routes import chatbot_bp
app.register_blueprint(chatbot_bp)
