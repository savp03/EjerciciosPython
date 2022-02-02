# Exercise 9 
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

def run():
    # numero=random.randint(1, 9)
    numero=3
    numero_usuario=0

    
    while numero!= numero_usuario:
        numero_usuario=int(input("Tienes que adivinar un numero del 1 al 9. Escribe tu numero: "))
       
        if numero<numero_usuario:
            print("Estas por encima del numero")
            numero_usuario=int(input("Intenta de nuevo. Escribe tu numero: "))             
        elif numero>numero_usuario:
            print("Estas por debajo del numero")
            numero_usuario=int(input("Intenta de nuevo. Escribe tu numero: "))
        else:
            print("Ganaste. El numero es: "+str(numero))  


if __name__=="__main__":
    run()




