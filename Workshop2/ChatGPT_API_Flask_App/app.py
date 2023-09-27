from flask import Flask, request, render_template
import requests
import json
import openai

app = Flask(__name__)

# Replace YOUR_API_KEY_HERE with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [{"role": "user", "content": user_input}]
        )
        response_text = response['choices'][0]['message']['content'].strip().replace('\n', '<br>')
        return render_template('index.html', chatGPT_response=response_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
