import random as r
import string

caratteri_speciali = ["@", "!", "#", "$", "%", "'", "-", "/", "=", "^", "_", "`", "{", "}", "~", "+", "\\"]
password = []

# open/open modes
# key = open("pass.txt", "w")
# modes:
# r = open for read (Default)
# w = open for write, truncate
# r+ = open for read/write
# w+ = open for read/write, truncate
# a+ = open for read/append


def generatore(lunghezza_password, scelta):
    for i in range(lunghezza_password):
        choose = r.choice(scelta)
        if choose == 1:
            password.append(r.choice(string.ascii_letters.lower()))  # genera caratteri di codice ashii in minuscolo (string.ascii_letters.lower()) è una funzione della libreria string, mentre random.choice (funzione della libreria random)
        elif choose == 2:
            password.append(r.choice(string.ascii_letters.upper()))  # genera caratteri di codice ashii in maiscolo (string.ascii_letters.upper) è una funzione della libreria string, mentre random.choice (funzione della libreria random)
        elif choose == 3:
            password.append(r.choice(caratteri_speciali))
        elif choose == 4:
            password.append(r.randrange(0, 10))

    pass_finale = str(password[0])
    for i in range(1, lunghezza_password):
        pass_finale = pass_finale + str(password[i])

    key = open("pass.txt", "w")
    key.write(f"La sua password generata e la seguente: {pass_finale} [{lunghezza_password}]")
    key.close()
