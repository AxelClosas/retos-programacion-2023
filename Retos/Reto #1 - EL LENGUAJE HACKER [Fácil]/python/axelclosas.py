'''
# Reto #1: EL "LENGUAJE HACKER"
#### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23

## Enunciado

```
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

    Objetivos:
    1. Lograr la transformación con letras unicamente
    2. Incluir transformación de números

    
    Traducción basica:
    Reemplaza las vocales nada más 

    Traducción Intermedia
    Reemplaza vocales y consonantes

    Traducción Avanzada:
    Reemplaza vocales, consonantes y números
'''


vocales = {
    'A': 4,
    'E': 3,
    'I': 1,
    'O': 0,
    'U': '(_)',
}
alfabeto = {
    'A': 4,
    'B': 'I3',
    'C': '[',
    'D': ')',
    'E': 3,
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': 1,
    'J': ',_|',
    'K': '>|',
    'L': 1,
    'M': '/\\/\\',
    'N': '^/',
    'O': 0,
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': 5,
    'T': 7,
    'U': '(_)',
    'V': '\/',
    'W': '\\/\/',
    'X': '><',
    'Y': 'j',
    'Z': 2,
    1: 'L',
    2: 'R',
    3: 'E',
    4: 'A',
    5: 'S',
    6: 'b',
    7: 'T',
    8: 'B',
    9: 'g',
    0: 'o',
}

# def checkType():
#     pass


# def invertLowerToUpper(c):
#     if c.isUpper():
#         pass

# Retorna una lista de caracteres en base a la lista de palabras recibidas.
def returnToCharacterList(words_list):
    charList = []
    for word in words_list:
        charList.extend([c for c in word])
        charList.append(" ")

    return charList


def convertTextToLeetSpeak(cadena):
    charList = returnToCharacterList(cadena)
    result = []
    for char in charList:
        if char == ' ':
            result.append(char)
            continue
        if char in alfabeto.keys():
            result.append(alfabeto[char])

    return result


def main():
    # Mensaje de bienvenida
    print("Bienvenidx. \n\n Este es un software que te permite traducir un mensaje escrito en lenguaje natural a lenguaje leet (1337).\n\n")

    # Solicitamos al usuario que ingrese el texto que desea transformar y las convertimos en mayusculas
    text = input('Mensaje: ').upper()

    # Validamos que se haya ingresado un text 
    if len(text) == 0:
        print('Error. Debes ingresar al menos un caracter.')
        exit()
    
    # Quitamos los espacios al inicio y final del texto
    text = text.strip()
    
    print("Mensaje ingresado:\n", text, "\n")

    # Separamos por palabras el texto ingresado
    words_list = text.split(sep=" ")
    
    # Transformamos el mensaje mediante la función convertTextToLeetSpeak que recibe como argumento el texto ingresado. Retorna una lista.
    msg_leet_on_list = convertTextToLeetSpeak(words_list)

    print(msg_leet_on_list)

    
    # Recibo el parametro c y retorno de manera implicita la conversión a string 
    # convert = lambda c : str(c)

    # Llamo la función convert y reemplazo los valores de salida mediante un nuevo list comprehension
    # 2da versión. Directamente convierto el valor mediante la función str()

    mensaje_leet = "".join([str(c) for c in msg_leet_on_list])

    print("Mensaje 1337 (or leet):\n", mensaje_leet, "\n")


if __name__ == '__main__':
    main()