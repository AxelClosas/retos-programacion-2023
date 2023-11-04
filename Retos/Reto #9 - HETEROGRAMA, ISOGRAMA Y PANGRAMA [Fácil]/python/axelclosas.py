'''
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

 Términos relacionados
Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.3​ Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente.

Un pangrama (del griego pan, 'todo' y gramma, 'letra') es una frase en la que aparecen todas las letras del abecedario. Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto.

'''
import string

# A B C D E
# F G H I J
# K L M N Ñ
# O P Q R S
# T U V W X
# Y Z

alfabeto = string.ascii_lowercase + 'áéíóúñ'
print(alfabeto)
lista_de_heterogramas = ["calumbrientos", "centrifugados", "centrifugamos", "configurables", "fecundizarlos", "profundizaste", "vomipurgantes"]

lista_de_isogramas = [ "murciélago", "huevo", "zafiro", "guitarra", "piedra", "acondicionar", "escritura", "intestinos", "papelera", "deed", "Vivienne", "Caucasus", "intestines", "deeded", "sestettes", "PUBVEXINGFJORD-SCHMALTZY"]



lista_de_pangramas = [
    "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja.",
    "Extraño pan de col y kiwi se quemó bajo fugaz vaho",
    "Jovencita, ¿qué zambullida exquisita en el fétido río de tu cuerpo fruncido?",
]


def es_heterograma(frase):
    lista_de_frecuencias = {}

    for l in frase:
        if l.lower() in lista_de_frecuencias.keys():
            lista_de_frecuencias[l.lower()] += 1
        else:
            lista_de_frecuencias[l.lower()] = 1

    for f in lista_de_frecuencias.values():
        if f != 1:
            return False
        
    return True


def test_heterograma():
    for palabra in lista_de_heterogramas:
        if es_heterograma(palabra):
            print(f"{palabra}: Heterograma")
        else:
            print(f"{palabra}: NO heterograma")


'''
Puede ser una frase
'''
def es_isograma(frase):
    lista_de_frecuencias = {}

    for l in frase:
        if l.lower() in lista_de_frecuencias.keys():
            lista_de_frecuencias[l.lower()] += 1
        else:
            lista_de_frecuencias[l.lower()] = 1

    def es_seg_orden():
        for f in lista_de_frecuencias.values():
            if f != 2:
                return False
        return True
    
    def es_tercer_orden():
        for f in lista_de_frecuencias.values():
            if f != 3:
                return False
        return True
    
    if es_heterograma(frase):
        return f"{frase}: Isograma de Primer Orden o Heterograma"
    elif es_seg_orden():
        return f"{frase}: Isograma de Segundo Orden"
    elif es_tercer_orden():
        return f"{frase}: Isograma de Tercer Orden"
    
    return f"{frase}: La palabra o frase ingresada no es un Isograma"


def test_isograma():
    for palabra in lista_de_isogramas:
        print(es_isograma(palabra))


def es_pangrama(frase):
    frase = frase.strip()
    
    for l in alfabeto:
        if l in frase:
            continue
        else:
            return False

    return True


def test_pangrama():
    for pangrama in lista_de_pangramas:         
        pangrama = pangrama.lower()   
        if es_pangrama(pangrama):
            print(f"{pangrama[:7]}...: Es un pangrama")
        else:   
            print("NO es un pangrama")


# test_heterograma()
# print("\n")

# test_isograma()
# print("\n")

test_pangrama()
print("\n")