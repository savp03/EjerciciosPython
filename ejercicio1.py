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