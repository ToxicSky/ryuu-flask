from flask import Blueprint, jsonify, request
from app.models.Location import Location
from app.serializers.location_schema import LocationSchema
from flask_jwt import jwt_required

locations = Blueprint('locations', __name__)


@locations.route('/api/locations')
def index():
    locations = Location.query.all()
    schema = LocationSchema(many=True)
    return jsonify(schema.dump(locations).data)


@locations.route('/api/locations/<int:location_id>')
def get(location_id):
    locations = Location.query.filter_by(id=location_id).first()
    schema = LocationSchema()
    return jsonify(schema.dump(locations).data)


@locations.route('/api/locations/search')
def search():
    name = request.args.get('name')
    locations = Location.query.filter_by(name=name).all()
    schema = LocationSchema(many=True)
    return jsonify(schema.dump(locations).data)


@locations.route('/api/locations', methods=['POST'])
@jwt_required()
def post():
    location_data = request.json.get('location', None)


@locations.route('/api/locations/<int:location_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def put(location_id):
    payload = request.json
    print(payload)
    return jsonify(dict())
