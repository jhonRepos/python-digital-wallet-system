from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance

db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the given Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
