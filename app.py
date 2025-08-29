# app.py
from flask import Flask, request, render_template
from halis_logic import generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html', bot_message='', user_message='')

@app.route('/chat', methods=['GET','POST'])
def chat():
    """
    Main chat route:
    - Receives user messages
    - Generates Halis response using halis_logic.py
    - Returns updated chat page
    """
    bot_reply = ''
    user_message = ''
    
    if request.method == 'POST':
        # Get user input from form
        user_message = request.form['message']
        
        # Generate Halis response
        bot_reply = generate_response(user_message)
    
    # Render chat page with both user message and bot reply
    return render_template(
        'chat.html',
        bot_message=bot_reply,
        user_message=user_message
    )

if __name__ == '__main__':
    # Run app locally for testing
    app.run(debug=True)
