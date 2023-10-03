'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

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
        elif char.isnumeric():
            char = int(char)
            result.append(alfabeto[char])

    return result


def main():
    # Mensaje de bienvenida
    print("\n")
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

    # Aplicando el metodo .join(<iterable>), que recibe un iterable como argumento, le podemos pasar un list comprehension para transformar un list a un string
    mensaje_leet = "".join([str(c) for c in msg_leet_on_list]).strip()

    print("Mensaje 1337 (or leet):\n", mensaje_leet, "\n")


if __name__ == '__main__':

    main()