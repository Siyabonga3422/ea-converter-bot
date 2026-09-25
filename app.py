from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>EA Converter Bot is Live!</h1><p>Your bot is working.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
