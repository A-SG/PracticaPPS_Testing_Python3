import unittest
import random
import string
from app.scripts.charfun import es_palindromo


def generar_palindromo(longitud):
    """Genera un palíndromo aleatorio de una longitud dada."""
    mitad = ''.join(random.choices(string.ascii_lowercase, k=longitud // 2))
    if longitud % 2 == 0:
        return mitad + mitad[::-1]
    else:
        return mitad + random.choice(string.ascii_lowercase) + mitad[::-1]

def generar_no_palindromo(longitud):
    """Genera una cadena aleatoria que no es un palíndromo."""
    cadena = ''.join(random.choices(string.ascii_lowercase, k=longitud))
    # Asegurarse de que no sea un palíndromo
    while cadena == cadena[::-1]:
        cadena = ''.join(random.choices(string.ascii_lowercase, k=longitud))
    return cadena

class TestEsPalindromo(unittest.TestCase):
    #Prueba que las cadenas palíndromas sean correctamente identificadas.
    def test_palindromos(self):
        palindromos = [
            "Anita lava la tina",  # Palíndromo con espacios
            "A mamá Roma le aviva el amor a mamá",  # Con tildes y espacios
            "Able was I, ere I saw Elba",  # Con caracteres no alfabéticos
            "No 'x' in Nixon",  # Con caracteres especiales
            "radar",  # Palíndromo simple
            "civic",  # Palíndromo simple
            "Was it a car or a cat I saw?",  # Con caracteres no alfabéticos
            "Madam, in Eden, I’m Adam",  # Con puntuación y mayúsculas
            "A Toyota's a Toyota",  # Con apóstrofes
            "tését",  # Palíndromo con caracteres Unicode
            "¿Acaso hubo búhos acá?",  # Palíndromo con acentos y caracteres especiales
            "🌟💥✨💥🌟"  # Palíndromo con emojis
        ]
        
        for palabra in palindromos:
            resultado = es_palindromo(palabra)
            self.assertTrue(resultado, f"Se esperaba que '{palabra}' fuera un palíndromo, pero la función devolvió {resultado}.")

    #Prueba que las cadenas no palíndromas sean correctamente identificadas.
    def test_no_palindromos(self):
        no_palindromos = [
            "Hola mundo",  # No es un palíndromo
            "Python",  # No es un palíndromo
            "Este es un test",  # No es un palíndromo
            "¡Viva México!",  # No es un palíndromo con signos de exclamación
            "Este no es un palíndromo",  # No es un palíndromo con múltiples palabras
            "No palindrome here!"  # No es un palíndromo
        ]
        
        for palabra in no_palindromos:
            resultado = es_palindromo(palabra)
            self.assertFalse(resultado, f"Se esperaba que '{palabra}' no fuera un palíndromo, pero la función devolvió {resultado}."
            )

    #Prueba que la cadena vacía se considere un palíndromo.
    def test_cadena_vacia(self):
        resultado = es_palindromo("")  
        self.assertTrue(resultado, f"Se esperaba que la cadena vacía fuera un palíndromo, pero la función devolvió {resultado}."
        )
    #Prueba que no haya diferencia entre mayúsculas y minúsculas.
    def test_mayusculas_y_minusculas(self):
        resultado = es_palindromo("Madam")  
        self.assertTrue(resultado, f"Se esperaba que 'Madam' fuera un palíndromo, pero la función devolvió {resultado}."
        )

    #Prueba que los espacios no afecten el resultado del palíndromo.
    def test_espacios(self):
        resultado = es_palindromo("  a man a plan a canal panama  ")  
        self.assertTrue(resultado, f"Se esperaba que '  a man a plan a canal panama  ' fuera un palíndromo, pero la función devolvió {resultado}.")

    #Prueba que las tildes sean ignoradas correctamente.
    def test_tildes(self):
        resultado = es_palindromo("Salas")  
        self.assertTrue(resultado, f"Se esperaba que 'Salas' fuera un palíndromo, pero la función devolvió {resultado}.")

    #Prueba con cadenas que contienen números.
    def test_numeros(self):
        palindromos_numeros = [
            "12321",  # Palíndromo de números
            "1a2b3b2a1"  # Palíndromo alfanumérico
        ]
        
        for cadena in palindromos_numeros:
            resultado = es_palindromo(cadena)
            self.assertTrue(resultado, f"Se esperaba que '{cadena}' fuera un palíndromo, pero la función devolvió {resultado}."
            )
        
        no_palindromos_numeros = [
            "12345",  # No es palíndromo
            "1234a567"  # No es palíndromo
        ]
        for cadena in no_palindromos_numeros:
            resultado = es_palindromo(cadena)
            self.assertFalse(resultado, f"Se esperaba que '{cadena}' no fuera un palíndromo, pero la función devolvió {resultado}.")


    #Prueba con caracteres especiales y puntuación.
    def test_caracteres_especiales(self):
        palindromos_caracteres = [
            "Eva, can I see bees in a cave?", # Palíndromo con puntuación
            "Mr. Owl ate my metal worm!"  # Palíndromo con puntuación
        ]
        
        for cadena in palindromos_caracteres:
            resultado = es_palindromo(cadena)
            self.assertTrue(resultado, f"Se esperaba que '{cadena}' fuera un palíndromo, pero la función devolvió {resultado}."
            )
        
        no_palindromos_caracteres = [
            "Hello, world!",  
            "This is not a palindrome."  
        ]
        
        for cadena in no_palindromos_caracteres:
            resultado = es_palindromo(cadena)
            self.assertFalse(resultado, f"Se esperaba que '{cadena}' no fuera un palíndromo, pero la función devolvió {resultado}.")

    #Prueba con combinaciones más complejas de caracteres.
    def test_combinaciones_complejas(self):
        resultado = es_palindromo("2A man, a plan, a canal, Panama! 2")  
        self.assertTrue(resultado, f"Se esperaba que '2A man, a plan, a canal, Panama! 2' fuera un palíndromo, pero la función devolvió {resultado}."
        )

    #Prueba con cadenas muy largas para verificar rendimiento y exactitud.
    def test_palindromos_largos(self):
        resultado = es_palindromo("a" * 10000 + "b" + "a" * 10000)  
        self.assertTrue(resultado, f"Se esperaba que la cadena larga fuera un palíndromo, pero la función devolvió {resultado}."
        )

        resultado = es_palindromo("a" * 10000 + "c" * 10000)  
        self.assertFalse(
            resultado, f"Se esperaba que la cadena larga no fuera un palíndromo, pero la función devolvió {resultado}.")
        
        # Test para generar 5 palíndromos aleatorios.
    def test_generar_palindromos(self):
        for _ in range(5):
            longitud = random.randint(3, 10)
            palindromo = generar_palindromo(longitud)
            self.assertEqual(palindromo, palindromo[::-1], f"Se esperaba que {palindromo} fuera un palíndromo, pero no lo es.")

    # Test para generar 5 cadenas no palíndromas aleatorias.
    def test_generar_no_palindromos(self):
        for _ in range(5):
            longitud = random.randint(3, 10)
            no_palindromo = generar_no_palindromo(longitud)
            self.assertNotEqual(no_palindromo, no_palindromo[::-1], f"Se esperaba que {no_palindromo} no fuera un palíndromo, pero lo es.")

if __name__ == "__main__":
    unittest.main()
