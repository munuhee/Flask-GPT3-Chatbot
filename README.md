# GPT-3 Chatbot using Flask and WebSockets

This project demonstrates a simple chatbot using OpenAI's GPT-3 powered by Flask and WebSockets.

## Requirements

- Python 3.x
- OpenAI API Key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/munuhee/Flask-GPT3-Chatbot.git
    cd Flask-GPT3-Chatbot
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    # On macOS and Linux
    python3 -m venv venv

    # On Windows
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    # On macOS and Linux
    source venv/bin/activate

    # On Windows
    .\venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up OpenAI API Key:

    - Get your OpenAI API key from [OpenAI](https://platform.openai.com/account/api-keys).
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=your_openai_api_key_here
        ```
    - Replace `your_openai_api_key_here` with your actual API key.

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
    - `routes.py`: Defines routes and WebSocket event handling.
    - `templates/`: Holds HTML templates (`index.html` for chat interface).
    - `static/`: Contains static files (JavaScript, CSS).
- `requirements.txt`: Lists dependencies for the Flask app.
- `run.py`: Script to start the Flask development server.

## Customization

- You can modify the conversation flow, UI/UX, and add additional functionalities as per your requirements.
- Explore and modify the OpenAI GPT-3 configurations in `openai_integration.py` to suit your needs.
