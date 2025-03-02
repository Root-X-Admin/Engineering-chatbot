from flask import Flask, render_template
from routes import chatbot_bp

app = Flask(__name__)

# Add a secret key for session management
app.secret_key = "your_secret_key_here"

# Register the chatbot blueprint
app.register_blueprint(chatbot_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
