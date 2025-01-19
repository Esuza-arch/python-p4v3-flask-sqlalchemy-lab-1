# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):
    """
    Fetch an earthquake by ID.
    """
    earthquake = Earthquake.query.get(id)  # Query the database
    if earthquake:
        # Return the earthquake as a JSON response
        return jsonify(earthquake.to_dict()), 200
    else:
        # Return error if not found
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    """
    Fetch earthquakes with magnitude greater than or equal to the specified value.
    """
    # Query the database for matching earthquakes
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Prepare the list of matching earthquakes
    quake_list = [
        {"id": quake.id, "location": quake.location, "magnitude": quake.magnitude, "year": quake.year}
        for quake in earthquakes
    ]

    # Prepare and return the response
    response = {
        "count": len(quake_list),
        "quakes": quake_list
    }
    return jsonify(response), 200    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
