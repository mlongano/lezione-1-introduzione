//  Questo è un commento al codice...
//  Serve per descrivere le istruzioni che digito
//  con la parola def si definisce una Funzione
//  una funzione è una sequenza di istruzioni
//  Funzione di teletrasporto dell'agente
//  Per eseguire la funzione che ho scritto devo leggere il comando dalla chat
//  Con player.on_chat si associa un testo scritto nella chat ad una funzione
player.onChat("tele", function FunzioneDiTeletrasporto() {
    agent.teleportToPlayer()
    player.say("Teletrasporto dell'agente! Meraviglia!!")
})
//  Movimenti dell'agente
player.onChat("test", function MovimentoDiTest() {
    //  Agente in avanti
    agent.move(FORWARD, 5)
    //  Agente in alto
    agent.move(UP, 8)
    //  Agente indietro
    agent.move(BACK, 5)
    //  Agente in basso
    agent.move(DOWN, 8)
    //  Spostamento laterale a sinistra
    agent.move(LEFT, 3)
    //  Spostamento laterale a destra
    agent.move(RIGHT, 3)
    //  Rotazione verso sinistra di 90 °
    agent.turnLeft()
    //  Rotazione verso destra di 90 °
    agent.turnRight()
})
