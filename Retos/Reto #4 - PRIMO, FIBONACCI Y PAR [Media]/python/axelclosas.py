'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/
'''
import random

# 1 1 2 3 5 8 13 21
def es_fibonacci(num):
    a = 0
    b = 1
    c = 0
    fibo = []
    fibo.append(1)
    for i in range(1, num+1):
        c = a + b
        fibo.append(c)
        a = b
        b = c
        
    if num in fibo:
        return 'es fibonacci'
    else:
        return 'no es fibonacci'

def es_primo(num):
    primeros_numeros_primos = [2, 3, 5, 7]
    if num == 1:
        return 'no es primo'
    
    if num in primeros_numeros_primos:
        return 'es primo'
    
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        return 'es primo'
    
    return 'no es primo'



def es_par(num):
    if num % 2 == 0:
        return 'es par'
    else:
        return 'es impar'

def run():
    try:
        num = int(input('Ingresa un número: '))    
        msg = f'{num} {es_primo(num)}, {es_fibonacci(num)} y {es_par(num)}'
        print(msg)
    except ValueError:
        print('Ingresa un número.')


if __name__ == '__main__':
    run()