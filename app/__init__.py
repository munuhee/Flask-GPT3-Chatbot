from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from app.chatbot.routes import chatbot_bp
app.register_blueprint(chatbot_bp)

if __name__ == '__main__':
    socketio.run(app, debug=True)
