import requests
import subprocess
import os
import time

# URL de la API para obtener la hora
url = 'http://worldtimeapi.org/api/timezone/America/Buenos_aires'
# Función para obtener la fecha y la hora de internet
def obtener_hora_internet():
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        datetime_str = datos['datetime']
        # El formato que devuelve es: 2024-09-16T14:15:22.123456-04:00
        fecha, hora = datetime_str.split('T')
        hora = hora.split('.')[0]  # Eliminar la parte milisegundos
        return fecha, hora
    else:
        raise Exception("No se pudo obtener la hora de Internet.")