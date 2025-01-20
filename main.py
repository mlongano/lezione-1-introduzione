# Questo è un commento al codice...
# Serve per descrivere le istruzioni che digito


# con la parola def si definisce una Funzione
# una funzione è una sequenza di istruzioni


# Funzione di teletrasporto dell'agente
def FunzioneDiTeletrasporto():
    agent.teleport_to_player()
    player.say("Teletrasporto dell'agente! Meraviglia!!")


# Per eseguire la funzione che ho scritto devo leggere il comando dalla chat
# Con player.on_chat si associa un testo scritto nella chat ad una funzione
player.on_chat("tele", FunzioneDiTeletrasporto)


# Movimenti dell'agente
def MovimentoDiTest():
    # Agente in avanti
    agent.move(FORWARD, 5)
    # Agente in alto
    agent.move(UP, 8)
    # Agente indietro
    agent.move(BACK, 5)
    # Agente in basso
    agent.move(DOWN, 8)
    # Spostamento laterale a sinistra
    agent.move(LEFT, 3)
    # Spostamento laterale a destra
    agent.move(RIGHT, 3)
    # Rotazione verso sinistra di 90 °
    agent.turn_left()
    # Rotazione verso destra di 90 °
    agent.turn_right()


player.on_chat("test", MovimentoDiTest)
