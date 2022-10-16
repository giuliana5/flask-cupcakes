"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect to the db."""

    db.app = app
    db.init_app(app)

    with app.app_context():
        db.create_all()

class Cupcake(db.Model):
    """Cupcake info."""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False, unique=True)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def default_img(self):
        """Displays default img if no img was entered."""

        return self.image or DEFAULT_IMG
