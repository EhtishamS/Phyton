import generator as g

lunghezza_password = int(input("Quanto deve essere lunga la password\n> "))
scelta = []
opzioni = 1
almeno_uno = False

while opzioni != 0:
    opzioni = (int(input("""
Digitare un numero alla volta:

1. Caratteri in maiuscolo.
2. Caratteri in minuscolo.
3. Caratteri speciali.
4. Numeri.
0. Per finire. 
""")))
    if 1 <= opzioni <= 4:
        scelta.append(opzioni)
        almeno_uno = True
    elif opzioni == 0:
        if not almeno_uno:
            print("Scegliere almeno una opzione")
            opzioni = -1
    else:
        print("inserire un numero presente nel menu!")

g.generatore(lunghezza_password, scelta)
