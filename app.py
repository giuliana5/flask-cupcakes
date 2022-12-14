"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)

connect_db(app)
DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

@app.route("/")
def home():
    """Display home page."""

    return render_template("home.html",)

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

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create new cupcake."""

    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json.get("image") or DEFAULT_IMG
    )

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Update cupcake info."""

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Deletes the selected cupcake."""

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")
    