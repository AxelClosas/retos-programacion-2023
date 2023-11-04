'''
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
'''
import string

class TraductorAurebesh:
    def __init__(self):
        self.alfabeto = {
            'A':'AUREK', 'B':'BESH', 'C':'CRESH', 'D':'DORN', 'E':'ESK', 'F':'FORN', 'G':'GREK', 'H':'HERF', 'I':'ISK', 'J':'JENTH', 'K':'KRILL', 'L':'LETH', 'M':'MERN', 'N':'NERN', 'O':'OSK', 'P':'PETH', 'Q':'QEK', 'R':'RESH', 'S':'SENTH', 'T':'TRILL', 'U':'USK', 'V':'VEV', 'W':'WESK', 'X':'XESH', 'Y':'YIRT', 'Z':'ZEREK', 'CH':'CHEREK', 'AE':'ENTH', 'EO':'ONITH', 'KH':'KRENTH', 'NG':'NEN', 'OO':'ORENTH', 'SH':'SHEN', 'TH':'THESH'
        }
        self.alfabeto_b = {
            'AUREK':'A', 'BESH':'B', 'CRESH':'C', 'DORN':'D', 'ESK':'E', 'FORN':'F', 'GREK':'G', 'HERF':'H', 'ISK':'I', 'JENTH':'J', 'KRILL':'K', 'LETH':'L', 'MERN':'M', 'NERN':'N', 'OSK':'O', 'PETH':'P', 'QEK':'Q', 'RESH':'R', 'SENTH':'S', 'TRILL':'T', 'USK':'U', 'VEV':'V', 'WESK':'W', 'XESH':'X', 'YIRT':'Y', 'ZEREK':'Z', 'CHEREK':'CH', 'ENTH':'AE', 'ONITH':'EO', 'KRENTH':'KH', 'NEN':'NG', 'ORENTH':'OO', 'SHEN':'SH', 'THESH':'TH'
        }
    # Casos a consultar letra siguiente: c ch, a ae, e eo, k kh, n ng, o oo, s sh, t th

    def espanol_aurebesh(self, frase=''):
        aurebesh = ''
        for l in frase:
            if l not in string.whitespace and l not in string.punctuation and l not in string.digits:
                aurebesh += f'{self.alfabeto[l.upper()]}'
            else:
                aurebesh += f'{str(l)}'
        return aurebesh.capitalize()
    
    def aurebesh_espanol(self, frase=''):
        espanol = ''
        palabra = ''
        for l in frase:
            if l not in string.whitespace and l not in string.punctuation and l not in string.digits:
                palabra += str(l).upper()
                if palabra in self.alfabeto_b.keys():
                    espanol += f'{str(self.alfabeto_b[palabra])}'
                    palabra = ''
            else:
                espanol += str(l)
        return espanol.capitalize()


if __name__ == '__main__':
    traductor = TraductorAurebesh()
    op = int(input('Como deseas traducir?.\n1. Español a Aurebesh.\n2. Aurebesh a Español.\n\nOpción: '))
    if op == 1:
        frase = input('Ingresa tu frase para traducir: ')
        resultado = traductor.espanol_aurebesh(frase)
        print('*' * 40)
        print(resultado)
    elif op == 2:
        frase = input('Ingresa tu frase para traducir: ')
        resultado = traductor.aurebesh_espanol(frase)        
        print('*' * 40)
        print(resultado)
 