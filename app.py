# Dependecies
import os
from web_flask import create_app
from dotenv import load_dotenv


# Define app
load_dotenv()
app = create_app()


# Run app
if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST'), port=os.getenv('FLASK_PORT'), debug=os.getenv('DEBUG'))