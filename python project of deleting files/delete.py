import os

path = input("Immettere il path assoluto della directory dalla quale vuole eliminare i file: ")
extention = input("Quale estensione vuole eliminare: ")
lenght = len(extention)
files = os.listdir(path)
print(f"I file trovati sono gli seguenti: {files}")
print(files)

for i in files:
    cont = ''
    for j in range(1,lenght+1):
        k = j;
        j = j*-1;
        cont+=i[j]
    if(cont==extention):
        os.remove(path+"/"+i)

        