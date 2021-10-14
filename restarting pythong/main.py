import os

prev_path = os.getcwd()

fileName = input("Inserire il nome del file da trovare: ")
indirizzo = input("Inserire il path assoluto del file in magari posso trovarlo: ")

pathExistence = os.path.exists(indirizzo)

while not pathExistence:
    print("Perfavore inserire di nuovo il path, quello precendente non era valido:")
    indirizzo = input("Inserire il path assoluto del file in magari posso trovarlo: ")
    pathExistence = os.path.exists(indirizzo)

os.chdir(indirizzo)
files = os.listdir()
found = False

def checkFile(srcFile):



for i in files:
    if i == fileName:
        found = True
        break

    if os.path.isdir(i):
        if checkFile(indirizzo + "\\" + i):
            found = True
            break



