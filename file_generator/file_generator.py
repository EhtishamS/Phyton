import os

name = input("Tell me the name of the file that you want to create: ")

type_file = int(input("Choose which file do you want to make:\n1.c\n2.c++\n> "))

while type_file < 1 or type_file > 2:
    print("Try again! the number is not in the menu\n")
    type_file = int(input("Choose which file do you want to make:\n1.c\n2.c++\n> "))

if type_file == 1:
    if name in os.listdir():
        print("please choose another name this is already taken!")
    else:
        try:
            file = open(name + '.c', 'w')
            file.write("""#include<iostream>

int main(){
    
   return 0;
}
""")
            file.close()
        except FileNotFoundError:
            print("Try another name of the file this is not possible!")

else:
    if name in os.listdir():
        print("please choose another name this is already taken!")
    else:
        try:
            file = open(name + '.cpp', 'w')
            file.write("""#include<iostream>
        
using namespace std;

int main(){

return 0;
    }
        """)
            file.close()
        except FileNotFoundError:
            print("Try another name of the file this is not possible!")
