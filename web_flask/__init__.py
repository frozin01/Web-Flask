# Dependecies
import os
from flask import Flask
from dotenv import load_dotenv


# Create app function
def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_mapping(
        DB_HOST=os.getenv('DB_HOST'),
        DB_NAME=os.getenv('DB_NAME'),
        DB_PORT=os.getenv('DB_PORT'),
        DB_USER=os.getenv('DB_USER'),
        DB_PASS=os.getenv('DB_PASS')
    )

    @app.route('/')
    def home():
        return 'Hello, Flask!'

    return app