# Dependecies
import psycopg2
from flask import current_app, g


# Open DB connection
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=current_app.config['DB_HOST'],
            dbname=current_app.config['DB_NAME'],
            port=current_app.config['DB_PORT'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASS']
        )
        g.db.autocommit = True

    return g.db

# Close DB connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()