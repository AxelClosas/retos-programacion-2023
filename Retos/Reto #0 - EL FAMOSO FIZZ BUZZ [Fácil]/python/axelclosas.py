'''
# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado

```
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
'''

# Si es multiplo de 3, retorna True
def fizz(num):
    return num % 3 == 0

# Si es multiplo de 5, retorna True
def buzz(num):
    return num % 5 == 0

# Si es multiplo de 3 y multiplo de 5 a la vez, retorna True
def fizzbuzz(num):
    return num % 3 == 0 and num % 5 == 0


def run():
    for i in range(1,101):
        if fizzbuzz(i):
            print('fizzbuzz')
        elif fizz(i):
            print('fizz')
        elif buzz(i):
            print('buzz')
        else:
            print(i)
        

if __name__ == '__main__':
    run()