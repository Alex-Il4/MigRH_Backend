# main.py
import os # Necesario para os.getenv
from dotenv import load_dotenv # Para cargar las variables del .env
from flask import Flask, render_template # Flask y render_template
from flask_sqlalchemy import SQLAlchemy # Para la integración con la base de datos

# --- 1. Cargar variables de entorno ---
# Esto debe hacerse al principio de tu script principal
load_dotenv()

# --- 2. Inicializar la aplicación Flask ---
app = Flask(__name__)

# --- 3. Configurar Flask-SQLAlchemy ---
# Lee la URL de la base de datos de las variables de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Deshabilita el seguimiento de modificaciones para ahorrar recursos (recomendado)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- 4. Inicializar la instancia de SQLAlchemy con la aplicación ---
db = SQLAlchemy(app)

# --- 5. Importar y Registrar Blueprints ---
# Esto es CRUCIAL para que las rutas definidas en tus controladores sean accesibles
# Asegúrate de que 'controllers' sea un paquete (tenga __init__.py)
# y que 'hotel_controller.py' contenga 'hotel_bp'
from controllers.hotel_controller import hotel_bp
app.register_blueprint(hotel_bp)

# --- 6. Definir rutas directamente en main.py (si es necesario) ---
# Estas son tus rutas de ejemplo para las plantillas HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/')
@app.route('/projects/<base>')
def func_template(base=None):
    if base is None:
        return render_template('base.html', name="Ningún proyecto especificado")
    else:
        return render_template('base2.html', name=base)

# --- 7. Punto de entrada principal para ejecutar la aplicación ---
if __name__ == '__main__':
    # Asegúrate de que tus modelos están importados o accesibles para db.create_all()
    # Una forma sencilla es importar aquí los modelos que necesiten ser creados si no están ya importados por un Blueprint
    # Aunque en este caso, si hotel_controller.py ya importa Hotel, es suficiente.
    from models.Hotel import Hotel # Solo para asegurar que el modelo Hotel sea conocido por SQLAlchemy
                                # Esto es redundante si hotel_controller.py ya lo importa y el Blueprint se registra.
                                # Pero no hace daño y asegura que db.create_all() lo vea.

    # Dentro de un contexto de aplicación para operaciones con la base de datos
    with app.app_context():
        # db.create_all() crea las tablas definidas en tus modelos si no existen.
        # Es ideal para el desarrollo y la primera vez que configuras la BD.
        # En producción, usarías herramientas de migración (ej. Flask-Migrate).
        db.create_all()

    # Inicia el servidor de desarrollo de Flask
    # debug=True activa el modo de depuración, recarga automática, y el depurador interactivo.
    # Esto es seguro para desarrollo, pero NUNCA debe usarse en producción.
    app.run(debug=True)