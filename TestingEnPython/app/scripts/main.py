from app.scripts.charfun import es_palindromo

def main():
    #Aquí va el código del main
    while True:
        # Solicitar al usuario que ingrese una frase
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        
        # Verificar si el usuario quiere salir del programa
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Verificar si la frase es palíndroma utilizando la función es_palindromo
            if es_palindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
