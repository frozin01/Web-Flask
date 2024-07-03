from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST'), port=os.getenv('FLASK_PORT'), debug=os.getenv('DEBUG'))