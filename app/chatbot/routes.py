from flask import Blueprint, render_template
from flask_socketio import emit
from ..openai_integration import generate_response
from .. import socketio

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    user_message = message['data']
    bot_response = generate_response(user_message)
    emit('response', {'data': bot_response})
