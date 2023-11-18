# GPT-3 Chatbot using Flask and WebSockets

This project demonstrates a simple chatbot using OpenAI's GPT-3 powered by Flask and WebSockets.

## Requirements

- Python 3.x
- OpenAI API Key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/munuhee/Flask-GPT3-Chatbot.git
    cd your-chatbot-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up OpenAI API Key:

    - Get your OpenAI API key from [OpenAI](https://platform.openai.com/account/api-keys).
    - Replace `YOUR_OPENAI_API_KEY` in `app/openai_integration.py` with your actual API key.

## Usage

1. Run the application:

    ```bash
    python run.py
    ```

2. Access the chatbot interface:

    Open your browser and go to `http://localhost:5000/`.

3. Start chatting with the chatbot by typing messages and clicking "Send".

## Structure

- `app/`: Contains the Flask application.
    - `__init__.py`: Initializes the Flask app and SocketIO.
    - `openai_integration.py`: Handles interactions with OpenAI GPT-3 API.
    - `chatbot/`: Package for chatbot components.
        - `__init__.py`: Initializes the chatbot module.
        - `routes.py`: Defines routes and WebSocket event handling.
        - `templates/`: Holds HTML templates (e.g., `index.html` for chat interface).
    - `static/`: Contains static files (e.g., JavaScript, CSS).
        - `main.js`: Front-end JavaScript file for WebSocket interactions.
- `requirements.txt`: Lists dependencies for the Flask app.
- `run.py`: Script to start the Flask development server.

## Customization

- You can modify the conversation flow, UI/UX, and add additional functionalities as per your requirements.
- Explore and modify the OpenAI GPT-3 configurations in `openai_integration.py` to suit your needs.
