from flask import Flask, render_template, request
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    return render_template('chat.html', bot_message='', user_message='')

@app.route('/chat', methods=['GET','POST'])
def chat():
    bot_reply = ''
    user_message = ''
    if request.method == 'POST':
        user_message = request.form['message']
        # TODO: Connect to Rasa or AI backend
        bot_reply = 'This is a placeholder response from Halis.'
    return render_template('chat.html', bot_message=bot_reply, user_message=user_message)

# Temporary route to initialize database tables
@app.route('/init-db')
def init_db():
    try:
        db.create_all()
        return "Database tables created successfully!"
    except Exception as e:
        return f"Error creating tables: {e}"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
