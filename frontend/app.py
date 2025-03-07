from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my app!"

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.logger.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000, debug=False)