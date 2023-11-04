'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''
import string
import random
import sys

def run():
    print(
    '''
    Hola!
    Sigue los siguientes pasos para generar las contraseñas que desees.
    Paso 1: Escribe la longitud que desees. Puede estar entre 8 y 16 caracteres.
    Paso 2: Escribe los parametros que desees. Maximo 4. Por ejemplo: 1234 o 231 o 41
    Paso 3: Escribe la cantidad de contraseñas aleatorias que desees generar.

    Parametros:
        1. Letras minusculas
        2. Letras mayusculas
        3. Numeros del 0 al 9
        4. Signos de puntuación

    El resultado se guardará en un archivo llamado password.txt
    ''')
    try:    
        longitud = int(input('Longitud: '))
        parametros = str(input('Parametros: '))
        cantidad = int(input('Cantidad: '))
        if 8 <= longitud <= 16 and 1 <= len(parametros) <= 4 and cantidad > 0:
            generador = PasswordGenerator()
            generador.escribir_contrasena_aleatoria(parametros, longitud, cantidad)
        else:
            print('No se han podido generar las contraseñas, revisa los pasos a seguir.')
            sys.exit(1)
    except ValueError:
        print('Solo puedes ingresar números.')

class PasswordGenerator:
    def __init__(self):
        self.parametros = {
            1 : string.ascii_lowercase,
            2 : string.ascii_uppercase,
            3 : string.digits,
            4 : string.punctuation,
        }


    def generar_contrasena(self, parametros, longitud):
        comb = self.generar_combinacion(parametros)
        contrasena = ''.join(random.choice(comb) for _ in range(longitud))
        return contrasena
    

    def generar_combinacion(self, parametros):
        comb = ''
        for n in parametros:
            comb += self.parametros[int(n)]
        return comb


    def escribir_contrasena_aleatoria(self,parametros, longitud, cantidad):
        with open("passwords.txt", "w") as file:
            for _ in range(cantidad):
                password = self.generar_contrasena(parametros, longitud)
                file.write(password + "\n")


if __name__ == '__main__':
    run()