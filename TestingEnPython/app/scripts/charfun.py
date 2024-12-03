""" 
charfun.py
Programa que determina si una cadena proporcionada por el usuario es palíndroma. Para ello se preguntará por teclado al usuario tantas veces como quiera hasta que escriba la palabra salir.
Ultima Modificación. 30/11/2024
Autor. Alejandro Santos Gutiérrez
Dependencias. Unicodedata

"""
import unicodedata

def es_palindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    
    # Normalizar la cadena para eliminar tildes y convertir caracteres especiales
    cadena = unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode('ASCII')

    # Convertir la cadena a minúsculas y eliminar caracteres no alfanuméricos (como espacios, puntuación)
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())

    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]