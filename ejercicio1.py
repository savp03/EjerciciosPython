# Exercise 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


def run():
    nombre=input("Escribe tu nombre: ")
    edad=int(input("Escribe tu edad: "))
    fecha100=2022-edad+100
    def imprimir_mensaje():
        print(nombre+ """ en el año """+str(fecha100)+""" tendrás 100 años        
        """)
    imprimir_mensaje()
    repeticiones=int(input("Escribe un numero: "))
    for x in range(repeticiones):
        imprimir_mensaje()

if __name__=="__main__":
    run()