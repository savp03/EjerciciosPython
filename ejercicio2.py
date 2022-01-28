# def mensaje(numero):
#     numero=int(input("Escribe un numero: "))
#     return numero

def run():
    opcion_menu=int(input("""
    Este programa tiene 3 herramientas. 

        1-Saber si un numero es par
        2-Saber si un numero es divisible en 4
        3-Saber si la division de 2 numeros es exacta

    Elige la herramienta que quieras usar escribiendo su numero: """))

    if opcion_menu==1:
        numero=int(input("Escribe un numero: "))
        par_o_impar=numero%2    
        if par_o_impar==0:
            print("Tu numero es par")
        else:
            print("Tu numero es impar")
    elif opcion_menu==2:
        numero=int(input("Escribe un numero: "))
        divisible_cuatro=numero%4
        if divisible_cuatro==0:
            print("Tu numero es divisible entre 4")
        else:
            print("Tu numero no es divisible entre 4")
    elif opcion_menu==3:
        dividendo=int(input("Escribe el dividendo: "))
        divisor=int(input("Escribe el divisor: "))
        divisible=dividendo%divisor
        if divisible==0:
            print("Los 2 numero si soy divisibles entre si")
        else:
            print("Los 2 numeros no son divisibles entre si")
    else:
        print("Escribe una opcion valida.")


if __name__=="__main__":
    run()

