from calendar import Calendar


def detectar_viernes_trece(anio=1, mes=1):
    calendario = Calendar(firstweekday=0)

    for tupla_numdia_dia in calendario.itermonthdays2(anio, mes):
        num_dia, dia = tupla_numdia_dia
        if num_dia == 13 and dia == 4:
            return True

    return False

def test_detectar_viernes_trece():
    meses = range(1, 13)
    for mes in meses:
        print(detectar_viernes_trece(2023, mes))

test_detectar_viernes_trece()