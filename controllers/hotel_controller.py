from flask import Blueprint, jsonify, request
from models.Hotel import Hotel
from main import db

hotel_bp = Blueprint('hotel_bp', __name__, url_prefix='/api/hotels')

@hotel_bp.route('/', methods=['GET'])
def get_all_hotels():
    hotels = Hotel.query.all()
    hotels_data = [hotel.to_dict() for hotel in hotels]
    return jsonify(hotels_data)

@hotel_bp.route('/<int:hotel_id>', methods=['GET'])
def get_hotel_id(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return jsonify(hotel.to_dict())

@hotel_bp.route('/<string:ciudad>', methods=['GET'])
def get_hotels_by_ciudad(ciudad):
    hotels = Hotel.query.filter_by(ciudad=ciudad).all()
    if not hotels:
        return jsonify({'error': 'No se encontraron hoteles'})
    hotels_data = [hotel.to_dict() for hotel in hotels]
    return jsonify(hotels_data)