from app import app
from openai import OpenAI

client = OpenAI(api_key=app.config.get("OPENAI_API_KEY"))

def generate_response(user_input):
    prompt_text = f"The user said: {user_input}\nAI response:"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"
