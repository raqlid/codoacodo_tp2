# users/init_db.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebapp.settings')

import django
django.setup()

from users.models import Usuario

def initialize_data():
    # Crea usuarios de ejemplo
    Usuario.objects.create(nombre='Juan', apellido='Perez', dni='1234567890')
    Usuario.objects.create(nombre='Maria', apellido='Lopez', dni='0987654321')
    Usuario.objects.create(nombre='Sandro', apellido='Sanchez', dni='83850284939')
    Usuario.objects.create(nombre='Julian', apellido='Andrade', dni='78585593383')
    Usuario.objects.create(nombre='Marcos', apellido='Armando', dni='47292927852')
    Usuario.objects.create(nombre='Lautaro', apellido='Otero', dni='47292927852')
    Usuario.objects.create(nombre='Ramon', apellido='Perez', dni='21814430303')
    Usuario.objects.create(nombre='Nicolas', apellido='Bustamante', dni='34729293204')
    Usuario.objects.create(nombre='Walter', apellido='Cruzado', dni='37392022334')
    Usuario.objects.create(nombre='Ezequiel', apellido='Simpson', dni='28022273920')


if __name__ == '__main__':
    initialize_data()
