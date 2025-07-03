from flask import Blueprint, jsonify, request
from models.Hotel import Hotel
from main import db

hotel_bp = Blueprint('hotel_bp', __name__, url_prefix='/api/hotels')

@hotel_bp.route('/', methods=['GET']) #Obtener todos los hoteles
def get_all_hotels():
    hotels = Hotel.query.all()
    hotels_data = [hotel.to_dict() for hotel in hotels]
    return jsonify(hotels_data)

@hotel_bp.route('/<int:hotel_id>', methods=['GET']) #Obtener un hotel por su id
def get_hotel_id(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return jsonify(hotel.to_dict()), 200

@hotel_bp.route('/<string:ciudad>', methods=['GET']) #Obtener todos los hoteles de una ciudad
def get_hotels_by_ciudad(ciudad):
    hotels = Hotel.query.filter_by(ciudad=ciudad).all()
    if not hotels:
        return jsonify({'error': 'No se encontraron hoteles'})
    hotels_data = [hotel.to_dict() for hotel in hotels]
    return jsonify(hotels_data), 200

@hotel_bp.route('/filTh/<string:TipoHotel>', methods=['GET']) #Obtener todos los hoteles de un tipo de hotel
def get_hotels_by_tipoHotel(TipoHotel):
    hotels = Hotel.query.filter_by(TipoHotel=TipoHotel).all()
    if not hotels:
        return jsonify({'error': 'No se encontraron hoteles'})
    hotels_data = [hotel.to_dict() for hotel in hotels]
    return jsonify(hotels_data), 200

@hotel_bp.route('/newhotel', methods=['POST']) #Crear un nuevo hotel
def create_hotel():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Falta información'}), 400
    if not 'nombre_hotel' in data or not 'ciudad' in data or not 'tipoHotel' in data:
        return jsonify({'error': 'Falta información en el formulario'}), 400
    #Creando nuevo objeto de la clase Hotel
    new_hotel = Hotel(
        nombre_hotel=data['nombre_hotel'],
        descripcion=data['descripcion'],
        ciudad=data['ciudad'],
        precio_por_noche=data['precio_por_noche'],
        TipoHotel=data['tipoHotel'],
        servicios_exclusivos=data['servicios_exclusivos'],
        calificacion_estrellas=data['calificacion_estrellas'],
        capacidad_maxima=data['capacidad_maxima'],
        tematica=data['tematica']
    )
    db.session.add(new_hotel)
    db.session.commit()
    return jsonify(new_hotel.to_dict()), 201

@hotel_bp.route('/edit/<int:hotel_id>', methods=['PUT']) #Editar un hotel
def edit_hotel(hotel_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Falta información'}), 400
    if not 'nombre_hotel' in data:
        return jsonify({'error': 'Falta información en el formulario'}), 400
    hotel = Hotel.query.get_or_404(hotel_id)
    hotel.nombre_hotel = data['nombre_hotel']
    hotel.descripcion = data['descripcion']
    hotel.ciudad = data['ciudad']
    hotel.precio_por_noche = data['precio_por_noche']
    hotel.TipoHotel = data['tipoHotel']
    hotel.servicios_exclusivos = data['servicios_exclusivos']
    hotel.calificacion_estrellas = data['calificacion_estrellas']
    hotel.capacidad_maxima = data['capacidad_maxima']
    hotel.tematica = data['tematica']
    db.session.commit()
    return jsonify(hotel.to_dict()), 200

@hotel_bp.route('/delete/<int:hotel_id>', methods=['DELETE']) #Eliminar un hotel
def delete_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    db.session.delete(hotel)
    db.session.commit()
    return jsonify({'message': 'Hotel eliminado'}), 200

