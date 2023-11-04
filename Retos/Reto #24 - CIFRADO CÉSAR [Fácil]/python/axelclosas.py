'''
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
'''
import string

class cifradoCesar:
    def __init__(self):
        self.alfabeto = string.ascii_uppercase
    
    def codificar(self, texto, desp=0):
        resultado = ''
        if desp <= 26:    
            for l in texto:
                if l not in string.whitespace and l not in string.digits and l not in string.punctuation:
                    index = self.alfabeto.index(l)
                    index_desp = index + desp
                    if index_desp >= len(self.alfabeto):
                        nuevo_index = abs(index_desp - len(self.alfabeto))
                        resultado += f'{self.alfabeto[nuevo_index]}'
                    else:
                        resultado += f'{self.alfabeto[index_desp]}'
                else:
                    resultado += f'{l}'
        return resultado
    
    def decodificar(self, texto, desp=0):
        resultado = ''
        if desp <= 26:    
            for l in texto:
                if l not in string.whitespace and l not in string.digits and l not in string.punctuation:
                    index = self.alfabeto.index(l)
                    index_desp = index - desp
                    if index_desp >= 0:
                        resultado += f'{self.alfabeto[index_desp]}'
                    else:
                        resultado += f'{self.alfabeto[len(self.alfabeto) + index_desp]}'
                else:
                    resultado += f'{l}'
        return resultado
    
if __name__ == '__main__':
    try:
        code_cesar = cifradoCesar()
        op = int(input('Cifrado de Cesar.\nDeseas crear un mensaje codificado o decodificar un mensaje?.\n1.Codificar\n2.Decodificar\nOpción: '))        
        match op:
            case 1:
                txt = str(input('Mensaje: ')).upper()
                desp = int(input('Nivel desplazamiento: '))
                result = code_cesar.codificar(txt, desp)
                print(result)
            case 2:
                txt = str(input('Mensaje: ')).upper()
                desp = int(input('Nivel desplazamiento: '))
                result = code_cesar.decodificar(txt, desp)
                print(result)
            case _:
                print('Ups... Intenta ingresar 1 o 2 la próxima.')
    except ValueError:
        print('Ups... Intenta ingresar 1 o 2 la próxima.')
