def controllozero(controllo, vittoria):
    count0 = 0

    for k in range(3):
        for j in range(3):
            if controllo[k][j] != ' ':
                if controllo[k][j] == 0:
                    count0 = count0 + 1
        if count0 == 3:
            print("Ha vinto il secondo giocatore!")
            vittoria = True

        count0 = 0

    for k in range(3):
        for j in range(3):
            if controllo[j][k] != ' ':
                if controllo[j][k] == 0:
                    count0 = count0 + 1
        if count0 == 3:
            print("Ha vinto il secondo giocatore!")
            vittoria = True
        count0 = 0

    j = 0
    for k in range(3):
        if controllo[k][j] != ' ':
            if controllo[k][j] == 0:
                count0 = count0 + 1
        if count0 == 3:
            print("Ha vinto il secondo giocatore!")
            vittoria = True
        j = j + 1
    count0 = 0

    j = 2
    for k in range(3):
        if controllo[k][j] != ' ':
            if controllo[k][j] == 0:
                count0 = count0 + 1
        if count0 == 3:
            print("Ha vinto il secondo giocatore!")
            vittoria = True
        j = j - 1

    return vittoria


def controllouno(controllo, vittoria):
    count1 = 0

    for k in range(3):
        for j in range(3):
            if controllo[k][j] != ' ':
                if controllo[k][j] == 1:
                    count1 = count1 + 1
        if count1 == 3:
            print("Ha vinto il primo giocatore!")
            vittoria = True

        count1 = 0

    for k in range(3):
        for j in range(3):
            if controllo[j][k] != ' ':
                if controllo[j][k] == 1:
                    count1 = count1 + 1
        if count1 == 3:
            print("Ha vinto il primo giocatore!")
            vittoria = True
        count1 = 0

    j = 0
    for k in range(3):
        if controllo[k][j] != ' ':
            if controllo[k][j] == 1:
                count1 = count1 + 1
        if count1 == 3:
            print("Ha vinto il primo giocatore!")
            vittoria = True
        j = j + 1
    count1 = 0

    j = 2
    for k in range(3):
        if controllo[k][j] != ' ':
            if controllo[k][j] == 1:
                count1 = count1 + 1
        if count1 == 3:
            print("Ha vinto il primo giocatore!")
            vittoria = True
        j = j - 1

    return vittoria
