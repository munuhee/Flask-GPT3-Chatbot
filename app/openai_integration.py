import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    return response.choices[0].text.strip()
