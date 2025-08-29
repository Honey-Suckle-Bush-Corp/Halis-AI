# app.py
from flask import Flask, request, render_template, session
from halis_logic import generate_response

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Needed for session storage

@app.route('/')
def home():
    if 'history' not in session:
        session['history'] = []
    return render_template('chat.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    Handles chat interactions:
    - Stores session-limited conversation history
    - Uses Halis AI to respond
    """
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        user_message = request.form['message']
        session['history'].append({'role': 'user', 'message': user_message})

        # Generate Halis response with session context
        bot_reply = generate_response(user_message, context=session['history'])
        session['history'].append({'role': 'bot', 'message': bot_reply})

    return render_template('chat.html', history=session['history'])
    

if __name__ == '__main__':
    app.run(debug=True)
