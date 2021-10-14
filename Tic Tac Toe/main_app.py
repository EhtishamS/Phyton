import controlli
import stampa

p1 = 'O'
p2 = 'X'

# variabili
player = True
bg = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
controllo = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
non_rip = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
i = 0
vittoria = False

# ciclo cuore del programma
while i < 9 and not vittoria:
    if i % 2 == 0:
        player = True
    else:
        player = False

    if player:
        trovato = False
        scelta = int(input("tocca al primo giocatore inserire il blocco (1,9): "))
        if 1 <= scelta <= 9:
            if non_rip[scelta - 1] == 1:
                trovato = True
        while scelta < 1 or scelta > 9 or trovato:
            scelta = int(input("Posto gia occcupato o numero fuori range!\n\ntocca al primo giocatore inserire il blocco (1,9): "))
            if 1 <= scelta <= 9:
                if non_rip[scelta-1] != 1:
                    trovato = False

        non_rip[scelta-1] = 1
        cont = 0
        while scelta > 3:
            scelta = scelta - 3
            cont += 1
        scelta = scelta - 1

        controllo[cont][scelta] = 1

        bg[cont][scelta] = p1
        stampa.stamp(bg)

        risultato = controlli.controllouno(controllo, vittoria)
        if risultato:
            vittoria = True
    else:
        trovato = False
        scelta = int(input("tocca al secondo giocatore inserire il blocco (1,9): "))
        if 1 <= scelta <= 9:
            if non_rip[scelta - 1] == 1:
                trovato = True
        while scelta < 1 or scelta > 9 or trovato:
            scelta = int(input("Posto gia occcupato o numero fuori range!\n\ntocca al primo giocatore inserire il blocco (1,9): "))
            if 1 <= scelta <= 9:
                if non_rip[scelta-1] != 1:
                    trovato = False
        non_rip[scelta - 1] = 1
        cont = 0
        while scelta > 3:
            scelta = scelta - 3
            cont += 1
        scelta = scelta - 1

        controllo[cont][scelta] = 0
        bg[cont][scelta] = p2

        stampa.stamp(bg)

        risultato = controlli.controllozero(controllo, vittoria)
        if risultato:
            vittoria = True
    i = i + 1
else:
    if not vittoria:
        print("non ha vinto nessuno")
