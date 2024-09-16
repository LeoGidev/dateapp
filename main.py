import requests
import subprocess
import os
import time

# URL de la API para obtener la hora
url = 'http://worldtimeapi.org/api/timezone/America/Buenos_aires'
# Función para obtener la fecha y la hora de internet
def obtener_hora_internet():