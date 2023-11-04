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
    'A': '4',
    'B': 'I3',
    'C': '[',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '&',
    'H': '#',
    'I': '1',
    'J': ',_|',
    'K': '>|',
    'L': '1',
    'M': '/\\/\\',
    'N': '^/',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': 'I2',
    'S': '5',
    'T': '7',
    'U': '(_)',
    'V': '\/',
    'W': '\\/\/',
    'X': '><',
    'Y': 'j',
    'Z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o',
}

def convertTxtToLangLeet(texto):
    nuevoTexto = ""
    # Validamos que se haya ingresado un texto    
    for c in texto:
        if c == " ":
            nuevoTexto += f"{str(c)}"
            
        if c in alfabeto.keys():
            nuevoTexto += f"{alfabeto[str(c)]}"
        
    return nuevoTexto

def main():
    # Mensaje de bienvenida
    print("\n")
    print("Bienvenidx. \n\n Este es un software que te permite traducir un mensaje escrito en lenguaje natural a lenguaje leet (1337).\n\n")

    # Solicitamos al usuario que ingrese el texto que desea transformar y las convertimos en mayusculas
    mensaje = input('Mensaje: ').upper()
    
    print("\n")
    print("_" * 70)

    traduccion = convertTxtToLangLeet(mensaje)

    print(traduccion)
    print("\n")


if __name__ == '__main__':

    main()