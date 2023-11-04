'''
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
'''
def convertir_decimal_a_octal(num):
    octal = ''
    while num != 0:
        cociente = int(num / 8) # 91=730/8 # 11 # 1=11/8 # 0
        octal += f'{str(num % 8)}' # '' + '2' + '3' + '3' + '1'
        num = cociente # num=91 #num=11 # num=1 # 0    
    return int(octal[::-1])

def convertir_decimal_a_hexa(num):
    hexa = ''
    def letra_equivalente(resto):
        match resto:
            case 10:
                return 'A'
            case 11:
                return 'B'
            case 12:
                return 'C'
            case 13:
                return 'D'
            case 14:
                return 'E'
            case 15:
                return 'F'
    
    while num > 15:
        cociente = int(num / 16)
        resto = num % 16
        if resto >= 10 and resto <= 15:
            hexa += f'{letra_equivalente(resto)}'
        else:
            hexa += f'{str(resto)}'
        num = cociente

    if num >= 10 and num <= 15:
        hexa += f'{letra_equivalente(num)}'
    else:
        hexa += f'{str(num)}'

    return str(hexa[::-1])

if __name__ == '__main__':
    # test
    # for i in range(1, 101):
    #     print(f'{i} \t {convertir_decimal_a_octal(i)} \t {convertir_decimal_a_hexa(i)}')
    # caso de uso
    try:
        num = int(input("Numero a convertir: "))
        print(f'decimal: {num}\noctal: {convertir_decimal_a_octal(num)}\nhexadecimal: {convertir_decimal_a_hexa(num)}')
    except ValueError:
        print('Debes ingresar un numero entero.')
    