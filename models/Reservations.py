from main import db
# from models.Hotel import Hotel # No necesitas importar Hotel aquí si usas 'hotel_referencia' en el backref

class Reservation(db.Model):
    __tablename__ = 'Reservations'

    reservationId = db.Column('reservationID', db.Integer, primary_key=True)
    # Define la clave foránea que apunta al hotel
    # 'Hotels.hotelID' es el nombre de la tabla y la columna a la que apunta
    HotelID = db.Column('HotelID', db.Integer, db.ForeignKey('Hotels.hotelID', ondelete='CASCADE'), nullable=False)
    # ... otras columnas de Reservation ...

    def to_dict(self):
        return {
            'reservationId': self.reservationId,
            'HotelID': self.HotelID,
            'userId': self.userId,
            # ... otras columnas de Reservation ...
        }