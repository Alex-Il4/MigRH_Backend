# models/Hotel.py
from main import db # Asumiendo que db se importa desde main.py

class Hotel(db.Model):
    # Especifica el nombre exacto de la tabla en tu base de datos SQL Server
    __tablename__ = 'Hotels'

    # Mapea las columnas de la BD a atributos de Python
    # id_hotel o hotelId (en Python) -> hotelID (en BD)
    # db.Column('NombreRealEnBD', db.TipoDato)
    hotelId = db.Column('hotelID', db.Integer, primary_key=True) #
    nombre_hotel = db.Column('nombre_hotel', db.String(255), nullable=False) # (DB es varchar(255))
    descripcion = db.Column('descripcion', db.String(db.Text), nullable=True) # (DB es varchar(max), se mapea a Text en SQLAlchemy)
    ciudad = db.Column('ciudad', db.String(255), nullable=True) # (DB es varchar(255))
    precio_por_noche = db.Column('precio_por_noche', db.Numeric(38, 2), nullable=True) # (DB es numeric(38,2))
    TipoHotel = db.Column('TipoHotel', db.String(31), nullable=False) # (DB es varchar(31))
    servicios_exclusivos = db.Column('servicios_exclusivos', db.String(db.Text), nullable=True) # (DB es varchar(max), se mapea a Text)
    calificacion_estrellas = db.Column('calificacion_estrellas', db.Integer, nullable=True) #
    capacidad_maxima = db.Column('capacidad_maxima', db.Integer, nullable=True) #
    tematica = db.Column('tematica', db.String(255), nullable=True) # (Esta columna no estaba en tu modelo original)

    def __repr__(self):
        return f'<Hotel {self.nombre_hotel}>'

    def to_dict(self):
        return {
            'hotelId': self.hotelId,
            'nombre_hotel': self.nombre_hotel,
            'descripcion': self.descripcion,
            'ciudad': self.ciudad,
            'precio_por_noche': str(self.precio_por_noche) if self.precio_por_noche is not None else None, # Convertir Numeric a string para JSON
            'TipoHotel': self.TipoHotel,
            'servicios_exclusivos': self.servicios_exclusivos,
            'calificacion_estrellas': self.calificacion_estrellas,
            'capacidad_maxima': self.capacidad_maxima,
            'tematica': self.tematica # Asegúrate de añadirla aquí también si la usas
        }