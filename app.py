"""Flask app for Cupcakes"""
from flask import Flask, redirect, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)

connect_db(app)
DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

@app.route("/api/cupcakes")
def list_cupcakes():
    """List the different cupcakes."""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.order_by(Cupcake.rating).all()]

    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Retrieve cupcake info."""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())
    