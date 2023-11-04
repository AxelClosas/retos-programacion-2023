'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
El mejor de los casos:
P1: 15 - Love
P1: 30 - Love
P1: 40 - Love
P1: Ventaja P1
P1: Ha ganado el P1


'''

class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.puntos = 0


    def sumar_puntos(self, punto):
        self.puntos += punto
    
    # Retorna puntaje
    def ver_puntos(self):
        return self.puntos




class Marcador:
    # jugadores: Lista de instancias de clases u objetos
    # secuencia: Lista de Strings P1

    def __init__(self, jugadores):
        self.jugador_uno = jugadores[0] # 1
        self.jugador_dos = jugadores[1] # 2
        self.puntaje_inical = 0


    def set_marcador(self, secuencia):
        marcador = ""
        cont_jugador_uno = 0
        cont_jugador_dos = 0
        
        for valor in secuencia:
            match valor:
                case "P1":
                    if cont_jugador_uno >= 0 and cont_jugador_uno <= 1:
                        cont_jugador_uno += 1
                        self.jugador_uno.sumar_puntos(15)
                        marcador += f"{self.comparar_puntos(cont_jugador_uno, cont_jugador_dos)}"

                    elif cont_jugador_uno >= 2:
                        cont_jugador_uno += 1
                        self.jugador_uno.sumar_puntos(10)
                        marcador += f"{self.comparar_puntos(cont_jugador_uno, cont_jugador_dos)}"

                case "P2":
                    if cont_jugador_dos >= 0 and cont_jugador_dos <= 1:
                        cont_jugador_dos += 1
                        self.jugador_dos.sumar_puntos(15)
                        marcador += f"{self.comparar_puntos(cont_jugador_uno, cont_jugador_dos)}"

                    elif cont_jugador_dos >= 2:
                        cont_jugador_dos += 1
                        self.jugador_dos.sumar_puntos(15)

                        marcador += f"{self.comparar_puntos(cont_jugador_uno, cont_jugador_dos)}"
        return marcador
    
        
    # Retorna el contenido para el marcador
    def comparar_puntos(self, cont_jugador_uno, cont_jugador_dos):
        # Retorna Love para el primer punto de cualquiera
        if self.jugador_uno.puntos == 0:
            return f"Love - {self.jugador_dos.ver_puntos()}\n"
        
        if self.jugador_dos.puntos == 0:
            return f"{self.jugador_uno.ver_puntos()} - Love\n"
        # Retorna 15
        if self.jugador_uno.puntos >= 15 and self.jugador_uno.puntos <= 30:
            return f"{self.jugador_uno.ver_puntos()} - {self.jugador_dos.ver_puntos()}\n"
        
        if self.jugador_dos.puntos >= 15 and self.jugador_dos.puntos <= 30:
            return f"{self.jugador_uno.ver_puntos()} - {self.jugador_dos.ver_puntos()}\n"
        
        # Retorna Deuce, Ventaja o Ganador del partido
        if self.jugador_uno.puntos >= 40:
            if self.jugador_dos.puntos >= 40:                 
                if cont_jugador_uno == cont_jugador_dos:
                    return "Deuce\n"
                elif cont_jugador_uno > cont_jugador_dos:
                    dif = abs(cont_jugador_uno - cont_jugador_dos)
                    if dif == 1:
                        return f"\nVentaja de {self.jugador_uno.nombre}\n"
                    elif dif == 2:
                        return f"\nGana el partido: {self.jugador_uno.nombre}\n"
                else:
                    dif = abs(cont_jugador_uno - cont_jugador_dos)
                    if dif == 1:
                        return f"Ventaja de {self.jugador_dos.nombre}\n"
                    elif dif == 2:
                        return f"Gana el partido: {self.jugador_dos.nombre}\n"
            
            return f"{self.jugador_uno.ver_puntos()} - {self.jugador_dos.ver_puntos()}\n"


class Partido:
    def __init__(self, jugadores):
        self.marcador = Marcador([jugadores[0], jugadores[1]])

    def jugar(self, secuencia):
        return self.marcador.set_marcador(secuencia)


if __name__ == '__main__':
    # Instanciamos dos variables para la clase Jugador
    partido = Partido([Jugador('Axel', 25), Jugador('Lucia', 25)])
    partido_dos = Partido([Jugador('Damian', 25), Jugador('Nazarena', 25)])

    resultado_uno = partido.jugar(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])

    resultado_dos = partido_dos.jugar(["P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2"])

    print("Resultado uno:\n")
    print(resultado_uno)

    print("Resultado dos:\n")
    print(resultado_dos)
    

    # print(game.winner)